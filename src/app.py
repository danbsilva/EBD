from flask import Flask

app = Flask(__name__)


def create_app():

    @app.get('/')
    def index():
        return 'Minha primeira p[agina'

    return app