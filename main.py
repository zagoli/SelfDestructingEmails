# Jacopo Zagoli, 2023

import multiprocessing
import time

from app import app
from email_sender import sender, SmtpServerConfig

if __name__ == '__main__':
    smtp_server_config = SmtpServerConfig(
        smtp_server='smtp.gmail.com',
        port=587,
        sender_email='your-email@gmail.com',
        password='password'
    )
    images_server_address = 'http://localhost:8080'

    images_server = multiprocessing.Process(
        target=lambda: app.run(
            host='0.0.0.0',
            port=8080,
            debug=True,
            use_reloader=False
        )
    )
    images_server.start()
    time.sleep(1)  # to not mess with stdout output
    sender(smtp_server_config, images_server_address)
