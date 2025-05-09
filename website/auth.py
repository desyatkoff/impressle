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


import re
import difflib

import flask
import flask_login
import werkzeug

import config
import website
from . import extensions


auth = flask.Blueprint(
    name = "auth",
    import_name = __name__
)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        # Check if user enters correct data:
        # - Username (must be at least 4 symbols and not longer than 16 symbols)
        # - Password (must be at least 8 symbols and not longer than 32 symbols)
        # - About Me (must be at least 0 symbols and not longer than 64 symbols)
        # - Checks the "Terms of Service" and "Privacy Policy" checkbox


        username = flask.request.form.get("username")
        password = flask.request.form.get("password")
        about_me = flask.request.form.get("about-me")
        checkbox = flask.request.form.get("checkbox")


        if website.models.User.query.filter_by(username=username).first() is not None:
            flask.flash(
                message = "Username is already taken",
                category = "error"
            )
        elif len(username) < 4:
            flask.flash(
                message = "Username is too short",
                category = "error"
            )
        elif len(username) > 16:
            flask.flash(
                message = "Username is too long",
                category = "error"
            )
        elif len(password) < 8:
            flask.flash(
                message = "Password is too short",
                category = "error"
            )
        elif len(password) > 32:
            flask.flash(
                message = "Password is too long",
                category = "error"
            )
        elif len(about_me) > 64:
            flask.flash(
                message = "\"About Me\" is too long",
                category = "error"
            )
        elif checkbox != "on":
            flask.flash(
                message = "You have to read Terms of Service and Privacy Policy",
                category = "error"
            )
        elif not re.match(
                pattern = r"^[a-zA-Z0-9_]+$",
                string = username
            ):
            flask.flash(
                message = "Incorrect username",
                category = "error"
            )
        else:
            for disallowed_username in config.DISALLOWED_USERNAMES:
                if difflib.SequenceMatcher(
                        a = username,
                        b = disallowed_username
                    ).ratio() > 0.75:
                    flask.flash(
                        message = "Username is not allowed",
                        category = "error"
                    )


                    return flask.redirect(flask.url_for("auth.signup"))


            flask.flash(
                message = "Successfully created new account",
                category = "success"
            )


            new_user = website.models.User(
                username = username,
                password = werkzeug.security.generate_password_hash(
                    password = password,
                    method = "scrypt"
                ),
                about_me = about_me
            )


            extensions.db.session.add(new_user)
            extensions.db.session.commit()


            flask_login.login_user(
                user = new_user,
                remember = True
            )


            return flask.redirect(
                flask.url_for(
                    endpoint = "routes.user_profile",
                    username = new_user.username
                )
            )


    return flask.render_template(
        "signup.html",
        user = flask_login.current_user
    )


@auth.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        # Check if user enters correct data:
        # - Username
        # - Password
        #
        # Also, user cannot log in if their account is inactive or banned


        username = flask.request.form.get("username")
        password = flask.request.form.get("password")

        user = website.models.User.query.filter_by(username=username).first()


        if user is not None:
            if werkzeug.security.check_password_hash(user.password, password):
                flask_login.login_user(
                    user = user,
                    remember = True
                )


                if user.status == "inactive":
                    flask.flash(
                        message = "Account is inactive",
                        category = "error"
                    )


                    return flask.redirect(flask.url_for("routes.inactive"))
                elif user.status == "banned":
                    flask.flash(
                        message = "Account is banned",
                        category = "error"
                    )


                    return flask.redirect(flask.url_for("routes.banned"))
                else:
                    flask.flash(
                        message = "Successfully logged in",
                        category = "success"
                    )


                    return flask.redirect(
                        flask.url_for(
                            endpoint = "routes.user_profile",
                            username = user.username
                        )
                    )
            else:
                flask.flash(
                    message = "Invalid password",
                    category = "error"
                )
        else:
            flask.flash(
                message = "Account does not exist",
                category = "error"
            )


    return flask.render_template(
        "login.html",
        user = flask_login.current_user
    )


@auth.route("/logout")
@flask_login.login_required
def logout():
    flask.flash(
        message = "Successfully logged out",
        category = "success"
    )


    flask_login.logout_user()


    return flask.redirect(flask.url_for("auth.login"))

