#!usr/bin/env python3
#
# Copyright (C) 2025 Desyatkov Sergey
#
# This file is part of Impressle.
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
import flask_babel
import flask_login
import flask_sqlalchemy

import config
from . import extensions


app: flask.Flask


def get_locale():
    return flask.request.accept_languages.best_match(
        matches = [
            "en",
            "ru"
        ]
    )


def init_flask_app():
    global app


    from . import api
    from . import auth
    from . import admin
    from . import models
    from . import routes


    app = flask.Flask(
        import_name = __name__
    )
    app.config["SECRET_KEY"] = config.FLASK_SECRET
    app.config["BABEL_TRANSLATION_DIRECTORIES"] = config.BABEL_DIRS
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS


    extensions.login_manager.login_view = "auth.login"


    extensions.babel.init_app(
        app = app,
        locale_selector = get_locale
    )
    extensions.login_manager.init_app(
        app = app
    )
    extensions.db.init_app(
        app = app
    )


    app.register_blueprint(
        blueprint = api.api,
        url_prefix = "/api"
    )
    app.register_blueprint(
        blueprint = auth.auth,
        url_prefix = "/"
    )
    app.register_blueprint(
        blueprint = admin.admin,
        url_prefix = "/admin"
    )
    app.register_blueprint(
        blueprint = routes.routes,
        url_prefix = "/"
    )


    @extensions.login_manager.user_loader
    def load_user(id):
        return models.User.query.filter_by(id=int(id)).first()


    return app
