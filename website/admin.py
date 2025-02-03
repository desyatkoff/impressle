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
        user = website.models.User.query.filter_by(uid=flask_login.current_user.uid).first()
        secret_key = flask.request.form.get("secret-key")


        if secret_key == config.FLASK_SECRET:
            if user.rank == "Admin":
                flask.flash(
                    message = "Successfully accessed the Admin Panel",
                    category = "success"
                )

                access = True


                return flask.redirect(flask.url_for("admin.panel"))
            else:
                flask.flash(
                    message = "You are not an Admin",
                    category = "error"
                )
        else:
            flask.flash(
                message = "Incorrect Secret Key",
                category = "error"
            )


            return flask.redirect(flask.request.referrer)


    return flask.render_template(
        "access_admin.html",
        user = flask_login.current_user
    )


@admin.route("/panel", methods=["GET", "POST"])
def panel():
    if access:
        if flask.request.method == "POST":
            try:
                user_uid = flask.request.form.get("user-uid")
                user = website.models.User.query.filter_by(uid=user_uid).first()

                user.is_banned = True
            except:
                try:
                    picture_uid = flask.request.form.get("picture-uid")
                    picture = website.models.Picture.query.filter_by(uid=picture_uid).first()

                    picture.is_banned = True


                    picture_author = website.models.User.query.filter_by(uid=picture.author_uid).first()


                    picture_author.xp -= 1
                except:
                    try:
                        comment_uid = flask.request.form.get("comment-uid")
                        comment = website.models.Comment.query.filter_by(uid=comment_uid).first()

                        comment.is_banned = True


                        comment_author = website.models.User.query.filter_by(uid=comment.author_uid).first()


                        comment_author.xp -= 1
                    except:
                        flask.flash(
                            message = "No any data",
                            category = "error"
                        )


            website.db.session.commit()


        return flask.render_template(
            "admin.html",
            user = flask_login.current_user,
            users = website.models.User.query.all(),
            pictures = website.models.Picture.query.all(),
            likes = website.models.Like.query.all(),
            comments = website.models.Comment.query.all(),
            views = website.models.View.query.all()
        )
    else:
        return flask.redirect(flask.url_for("admin.access_admin"))
