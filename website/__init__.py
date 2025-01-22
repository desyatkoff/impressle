import os

import flask
import dotenv

import config
from .auth import auth
from .views import views


dotenv.load_dotenv(f"{config.PROJECT_ROOT_PATH}/.env")


FLASK_SECRET = os.getenv("FLASK_SECRET")


def init_flask_app():
    app = flask.Flask(import_name=__name__)
    app.secret_key = FLASK_SECRET

    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(views, url_prefix="/")


    return app
