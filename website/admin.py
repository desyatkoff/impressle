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
                    message = "Successfully accessed the admin panel",
                    category = "success"
                )

                access = True


                return flask.redirect(flask.url_for("admin.panel"))
            else:
                flask.flash(
                    message = "You are not an admin",
                    category = "error"
                )
        else:
            flask.flash(
                message = "Incorrect secret key",
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
            form_type = flask.request.form.get("form-type")


            if form_type == "edit-data":
                table_name = flask.request.form.get("table-name")
                row_id = flask.request.form.get("row-id")
                column_name = flask.request.form.get("column-name")

                new_value = flask.request.form.get("new-value")


                if table_name.lower() == "user":
                    item = website.models.User.query.filter_by(id=row_id).first()


                    if column_name.lower() == "id":
                        item.id = new_value
                    elif column_name.lower() == "uid":
                        item.uid = new_value
                    elif column_name.lower() == ("date_created" or "date created"):
                        item.date_created = new_value
                    elif column_name.lower() == "username":
                        item.username = new_value
                    elif column_name.lower() == "password":
                        item.password = new_value
                    elif column_name.lower() == ("about_me" or "about me"):
                        item.about_me = new_value
                    elif column_name.lower() == "karma":
                        item.karma = new_value
                    elif column_name.lower() == "rank":
                        item.rank = new_value
                    elif column_name.lower() == ("show_followers" or "show followers"):
                        item.show_followers = new_value
                    elif column_name.lower() == ("allow_comments" or "allow comments"):
                        item.allow_comments = new_value
                    elif column_name.lower() == "status":
                        item.status = new_value
                elif table_name.lower() == "picture":
                    item = website.models.Picture.query.filter_by(id=row_id).first()


                    if column_name.lower() == "id":
                        item.id = new_value
                    elif column_name.lower() == "uid":
                        item.uid = new_value
                    elif column_name.lower() == ("date_created" or "date created"):
                        item.date_created = new_value
                    elif column_name.lower() == "title":
                        item.title = new_value
                    elif column_name.lower() == ("image_data" or "image data"):
                        item.image_data = new_value
                    elif column_name.lower() == ("author_uid" or "author uid"):
                        item.author_uid = new_value
                    elif column_name.lower() == ("author_username" or "author username"):
                        item.author_username = new_value
                    elif column_name.lower() == "status":
                        item.status = new_value
                elif table_name.lower() == "follow":
                    item = website.models.Follow.query.filter_by(id=row_id).first()


                    if column_name.lower() == "id":
                        item.id = new_value
                    elif column_name.lower() == "uid":
                        item.uid = new_value
                    elif column_name.lower() == ("date_created" or "date created"):
                        item.date_created = new_value
                    elif column_name.lower() == ("followed_uid" or "followed uid"):
                        item.followed_uid = new_value
                    elif column_name.lower() == ("followed_username" or "followed username"):
                        item.followed_username = new_value
                    elif column_name.lower() == ("follower_uid" or "follower uid"):
                        item.follower_uid = new_value
                    elif column_name.lower() == ("follower_username" or "follower username"):
                        item.follower_username = new_value
                elif table_name.lower() == "like":
                    item = website.models.Like.query.filter_by(id=row_id).first()


                    if column_name.lower() == "id":
                        item.id = new_value
                    elif column_name.lower() == "uid":
                        item.uid = new_value
                    elif column_name.lower() == ("date_created" or "date created"):
                        item.date_created = new_value
                    elif column_name.lower() == ("picture_uid" or "picture uid"):
                        item.picture_uid = new_value
                    elif column_name.lower() == ("author_uid" or "author uid"):
                        item.author_uid = new_value
                    elif column_name.lower() == ("author_username" or "author username"):
                        item.author_username = new_value
                elif table_name.lower() == "comment":
                    item = website.models.Comment.query.filter_by(id=row_id).first()


                    if column_name.lower() == "id":
                        item.id = new_value
                    elif column_name.lower() == "uid":
                        item.uid = new_value
                    elif column_name.lower() == ("date_created" or "date created"):
                        item.date_created = new_value
                    elif column_name.lower() == "text":
                        item.text = new_value
                    elif column_name.lower() == ("author_uid" or "author uid"):
                        item.author_uid = new_value
                    elif column_name.lower() == ("author_username" or "author username"):
                        item.author_username = new_value
                    elif column_name.lower() == "status":
                        item.status = new_value
                elif table_name.lower() == "view":
                    item = website.models.View.query.filter_by(id=row_id).first()


                    if column_name.lower() == "id":
                        item.id = new_value
                    elif column_name.lower() == "uid":
                        item.uid = new_value
                    elif column_name.lower() == ("date_created" or "date created"):
                        item.date_created = new_value
                    elif column_name.lower() == ("picture_uid" or "picture uid"):
                        item.picture_uid = new_value
                    elif column_name.lower() == ("author_uid" or "author uid"):
                        item.author_uid = new_value
                    elif column_name.lower() == ("author_username" or "author username"):
                        item.author_username = new_value
            elif form_type == "ban-form":
                user_uid = flask.request.form.get("user-uid")
                picture_uid = flask.request.form.get("picture-uid")
                comment_uid = flask.request.form.get("comment-uid")


                try:
                    user = website.models.User.query.filter_by(uid=int(user_uid)).first()
                    user.status = "banned"
                except:
                    pass

                try:
                    picture = website.models.Picture.query.filter_by(uid=int(picture_uid)).first()
                    picture.status = "banned"

                    picture_author = website.models.User.query.filter_by(uid=picture.author_uid).first()
                    picture_author.karma -= 1
                except:
                    pass

                try:
                    comment = website.models.Comment.query.filter_by(uid=int(comment_uid)).first()
                    comment.status = "banned"

                    comment_author = website.models.User.query.filter_by(uid=comment.author_uid).first()
                    comment_author.karma -= 1
                except:
                    pass


            website.db.session.commit()


        return flask.render_template(
            "admin.html",
            user = flask_login.current_user,
            users = website.models.User.query.all(),
            pictures = website.models.Picture.query.all(),
            follows = website.models.Follow.query.all(),
            likes = website.models.Like.query.all(),
            dislikes = website.models.Dislike.query.all(),
            comments = website.models.Comment.query.all(),
            views = website.models.View.query.all()
        )
    else:
        return flask.redirect(flask.url_for("admin.access_admin"))
