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


import flask
import flask_login
import werkzeug

import website


auth = flask.Blueprint(
    name = "auth",
    import_name = __name__
)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        username = flask.request.form.get("username")
        password = flask.request.form.get("password")
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
        elif len(password) < 8:
            flask.flash(
                message = "Password is too short",
                category = "error"
            )
        elif checkbox is (False or None):
            flask.flash(
                message = "You have to read Terms of Service and Privacy Policy",
                category = "error"
            )
        else:
            flask.flash(
                message = "Successfully created new account",
                category = "success"
            )


            new_user = website.models.User(
                username = username,
                password = werkzeug.security.generate_password_hash(
                    password = password,
                    method = "scrypt"
                )
            )


            website.db.session.add(new_user)
            website.db.session.commit()


            flask_login.login_user(
                user = new_user,
                remember = True
            )


            return flask.redirect(
                flask.url_for(
                    endpoint = "views.user_profile",
                    username = new_user.username
                )
            )


    return flask.render_template("signup.html", user=flask_login.current_user)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        username = flask.request.form.get("username")
        password = flask.request.form.get("password")

        user = website.models.User.query.filter_by(username=username).first()


        if user is not None:
            if werkzeug.security.check_password_hash(user.password, password):
                if user.is_banned is True:
                    flask.flash(
                        message = "Account is banned",
                        category = "error"
                    )


                    return flask.redirect(flask.url_for("views.banned"))
                else:
                    flask.flash(
                        message = "Successfully logged in",
                        category = "success"
                    )

                    flask_login.login_user(
                        user = user,
                        remember = True
                    )


                    return flask.redirect(
                        flask.url_for(
                            endpoint = "views.user_profile",
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


    return flask.render_template("login.html", user=flask_login.current_user)


@auth.route("/logout")
@flask_login.login_required
def logout():
    flask.flash(
        message = "Successfully logged out",
        category = "success"
    )


    flask_login.logout_user()


    return flask.redirect(flask.url_for("auth.login"))
