# Jacopo Zagoli, 2023

import logging
from pathlib import Path

from flask import Flask, send_file

app = Flask(__name__)
logging.getLogger('werkzeug').disabled = True

__used_secrets = set()


@app.route('/')
def connection_test():
    return 'Flask works!'


@app.route('/secret/<image_name>')
def image(image_name: str):
    if image_name not in __used_secrets:
        __used_secrets.add(image_name)
        image_path = Path('images/qr') / image_name
        return send_file(image_path, mimetype='image/png')
    return send_file(Path('images/blocked.png'), mimetype='image/png')
