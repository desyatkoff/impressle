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

import config
import website


admin = flask.Blueprint(
    name = "admin",
    import_name = __name__
)

access = False


@admin.route("/", methods=["GET", "POST"])
def access_admin():
    global access


    if flask.request.method == "POST":
        secret_key = flask.request.form.get("secret-key")


        if secret_key == config.FLASK_SECRET:
            flask.flash(
                message = "Successfully accessed the Admin Panel",
                category = "success"
            )

            access = True


            return flask.redirect(flask.url_for("admin.panel"))
        else:
            flask.flash(
                message = "Incorrect Secret Key",
                category = "error"
            )


            return flask.redirect(flask.request.referrer)


    return flask.render_template("access_admin.html")


@admin.route("/panel")
def panel():
    if access:
        return flask.render_template(
            "admin.html",
            users = website.models.User.query.all(),
            pictures = website.models.Picture.query.all(),
            likes = website.models.Like.query.all(),
            comments = website.models.Comment.query.all()
        )
    else:
        return flask.redirect(flask.url_for("admin.access_admin"))
