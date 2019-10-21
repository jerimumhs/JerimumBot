from flask import Flask

from bot import JerimumBot


app = Flask(__name__)


@app.route('/')
def hello():
    JerimumBot.send_message(
        chat_id='-281314498',
        text='Essa é uma mensagem de teste'
    )
    return 'Hello, World!'
