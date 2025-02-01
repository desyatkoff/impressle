#!usr/bin/env python3
#
# Copyright (C) 2025 Desyatkov Sergey
#
# This file is part of impressle.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.


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
    from . import admin
    from . import models


    app = flask.Flask(__name__)
    app.config["SECRET_KEY"] = config.FLASK_SECRET
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS


    db.init_app(app)


    login_manager.login_view = "auth.login"
    login_manager.init_app(app)


    app.register_blueprint(admin.admin, url_prefix="/admin")
    app.register_blueprint(api.api, url_prefix="/api")
    app.register_blueprint(auth.auth, url_prefix="/")
    app.register_blueprint(views.views, url_prefix="/")


    @login_manager.user_loader
    def load_user(id):
        return models.User.query.filter_by(id=int(id)).first()


    return app
