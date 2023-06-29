import random
import smtplib
import string
from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import qrcode


@dataclass
class SmtpServerConfig:
    smtp_server: str
    port: int
    sender_email: str
    password: str


def _random_code(size: int):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=size))


def _generate_qrcode(images_path: Path, filename: str):
    content = 'Secret message: ' + _random_code(10)
    qr = qrcode.make(content)
    qr.save(images_path / (filename + '.png'))


def _send_email(smtp_server_config: SmtpServerConfig, receiver_email: str, email_content: str):
    with smtplib.SMTP(smtp_server_config.smtp_server, smtp_server_config.port) as server:
        server.starttls()
        server.login(smtp_server_config.sender_email, smtp_server_config.password)
        message = MIMEMultipart('alternative')
        message['Subject'] = 'One-time Secret!'
        message['From'] = smtp_server_config.sender_email
        message['To'] = receiver_email
        part1 = MIMEText('Only html is supported!', 'plain')
        part2 = MIMEText(email_content, 'html')
        message.attach(part1)
        message.attach(part2)
        try:
            server.sendmail(smtp_server_config.sender_email, receiver_email, message.as_string())
        except smtplib.SMTPException as e:
            print(e)


def _generate_email_content(image_id: str, images_server_address: str):
    return f'''
    <html>
        <h1>Enjoy your secret!</h1>
        <img src="{images_server_address}/secret/{image_id}.png" alt="secret code">
    </html>
    '''


def sender(smtp_server_config: SmtpServerConfig, images_server_address: str):
    while True:
        receiver_email = input('Insert an email address: ')
        if receiver_email == 'stop':
            break
        image_id = _random_code(7)
        print('Sending mail to', receiver_email, 'with image', image_id)
        _generate_qrcode(Path('images/qr'), image_id)
        _send_email(smtp_server_config, receiver_email, _generate_email_content(image_id, images_server_address))
