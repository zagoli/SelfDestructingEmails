import threading
from email_sender import sender, SmtpServerConfig

if __name__ == '__main__':
    smtp_server_config = SmtpServerConfig(
        smtp_server='smtp.gmail.com',
        port=587,
        sender_email='',
        password=''
    )
    images_server_address = ''
    mail_sender = threading.Thread(target=sender(smtp_server_config, images_server_address))
    mail_sender.start()