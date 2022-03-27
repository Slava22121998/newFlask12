import logging

from flask import Flask

from loader.loader import loader
from main.main import main

logging.basicConfig(filename='app.log', level='INFO')

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(loader)
if __name__ == '__main__':
    app.run()
