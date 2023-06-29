import logging

from flask import Flask

app = Flask(__name__)
logging.getLogger('werkzeug').disabled = True

__used_secrets = set()

@app.route('/secret/<image_name>')
def image(image_name: str):
    if image_name not in __used_secrets:
        __used_secrets.add(image_name)
        return f'Your secret is: {image_name}'
    return 'Used secret'
