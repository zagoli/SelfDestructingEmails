import random
import string
import qrcode
import smtplib
from pathlib import Path
from dataclasses import dataclass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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


def sender(smtp_server_config: SmtpServerConfig):
    while True:
        receiver_email = input('Insert an email address: ')
        if receiver_email == 'stop':
            break
        image_id = _random_code(7)
        print('Sending mail to', receiver_email, 'with image', image_id)
        # _generate_qrcode(Path('images'), image_id)
        _send_email(smtp_server_config, receiver_email, '<h1>CIAO</h1>')



if __name__ == '__main__':
    smtp_server_config = SmtpServerConfig(
        smtp_server='smtp.gmail.com',
        port=587,
        sender_email='',
        password=''
    )
    sender(smtp_server_config)