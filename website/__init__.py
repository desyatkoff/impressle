import os

import flask
import flask_login
import flask_sqlalchemy

import config


db = flask_sqlalchemy.SQLAlchemy()
login_manager = flask_login.LoginManager()

app: flask.Flask


def init_flask_app():
    global app


    from . import api
    from . import auth
    from . import views
    from . import models


    app = flask.Flask(__name__)
    app.config["SECRET_KEY"] = config.FLASK_SECRET
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS


    db.init_app(app)


    login_manager.login_view = "auth.login"
    login_manager.init_app(app)


    app.register_blueprint(api.api, url_prefix="/api")
    app.register_blueprint(auth.auth, url_prefix="/")
    app.register_blueprint(views.views, url_prefix="/")


    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))


    return app
