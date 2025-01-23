import os

import flask
import dotenv
import flask_login
import flask_sqlalchemy

import config


dotenv.load_dotenv(f"{config.PROJECT_ROOT_PATH}/.env")


FLASK_SECRET = os.getenv("FLASK_SECRET")

db = flask_sqlalchemy.SQLAlchemy()
login_manager = flask_login.LoginManager()


def init_flask_app():
    from . import auth
    from . import views
    from . import models


    app = flask.Flask(__name__)
    app.config["SECRET_KEY"] = FLASK_SECRET
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{config.PROJECT_ROOT_PATH}/database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


    db.init_app(app)


    login_manager.login_view = "auth.login"
    login_manager.init_app(app)


    app.register_blueprint(views.views, url_prefix="/")
    app.register_blueprint(auth.auth, url_prefix="/")


    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))


    return app
