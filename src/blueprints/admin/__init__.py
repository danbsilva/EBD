from flask import Blueprint
from src.app import app
bp_admin = Blueprint('admin', __name__, url_prefix='/admin')


def init_app():

    app.register_blueprint(bp_admin)

