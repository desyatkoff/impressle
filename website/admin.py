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


import flask
import flask_login

import config
import website
from . import extensions


admin = flask.Blueprint(
    name = "admin",
    import_name = __name__
)


@admin.route("/", methods=["GET", "POST"])
@flask_login.login_required
def panel():
    if flask_login.current_user.rank == "Admin":
        if flask.request.method == "POST":
            form_type = flask.request.form.get("form-type")


            if form_type == "edit-data":
                table_name = flask.request.form.get("table-name")
                item_uid = flask.request.form.get("item-uid")
                column_name = flask.request.form.get("column-name")
                new_value = flask.request.form.get("new-value")


                if table_name.lower() == ("user" or "users"):
                    item = website.models.User.query.filter_by(uid=item_uid).first()


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
                    elif column_name.lower() == ("show_status" or "show status"):
                        item.show_status == new_value
                    elif column_name.lower() == "status":
                        item.status = new_value
                elif table_name.lower() == ("picture" or "pictures"):
                    item = website.models.Picture.query.filter_by(uid=item_uid).first()


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
                    elif column_name.lower() == ("likes_count" or "likes count"):
                        item.likes_count = new_value
                    elif column_name.lower() == ("dislikes_count" or "dislikes count"):
                        item.dislikes_count = new_value
                    elif column_name.lower() == ("comments_count" or "comments count"):
                        item.comments_count = new_value
                    elif column_name.lower() == ("views_count" or "views count"):
                        item.views_count = new_value
                    elif column_name.lower() == ("downloads_count" or "downloads count"):
                        item.downloads_count = new_value
                    elif column_name.lower() == ("author_uid" or "author uid"):
                        item.author_uid = new_value
                    elif column_name.lower() == ("author_username" or "author username"):
                        item.author_username = new_value
                    elif column_name.lower() == "status":
                        item.status = new_value
                elif table_name.lower() == ("follow" or "follows"):
                    item = website.models.Follow.query.filter_by(uid=item_uid).first()


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
                elif table_name.lower() == ("like" or "likes"):
                    item = website.models.Like.query.filter_by(uid=item_uid).first()


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
                elif table_name.lower() == ("dislike" or "dislikes"):
                    item = website.models.Dislike.query.filter_by(uid=item_uid).first()


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
                elif table_name.lower() == ("comment" or "comments"):
                    item = website.models.Comment.query.filter_by(uid=item_uid).first()


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
                elif table_name.lower() == ("view" or "views"):
                    item = website.models.View.query.filter_by(uid=item_uid).first()


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
                elif table_name.lower() == ("download" or "downloads"):
                    item = website.models.Download.query.filter_by(uid=item_uid).first()


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
            elif form_type == "delete-form":
                user_uid = flask.request.form.get("user-uid")
                picture_uid = flask.request.form.get("picture-uid")
                comment_uid = flask.request.form.get("comment-uid")


                try:
                    user = website.models.User.query.filter_by(uid=int(user_uid)).first()
                    user.status = "deleted"
                except:
                    pass

                try:
                    picture = website.models.Picture.query.filter_by(uid=int(picture_uid)).first()
                    picture.status = "deleted"

                    picture_author = website.models.User.query.filter_by(uid=picture.author_uid).first()
                    picture_author.karma -= 1
                except:
                    pass

                try:
                    comment = website.models.Comment.query.filter_by(uid=int(comment_uid)).first()
                    comment.status = "deleted"

                    comment_author = website.models.User.query.filter_by(uid=comment.author_uid).first()
                    comment_author.karma -= 1
                except:
                    pass
            elif form_type == "real-delete-form":
                table_name = flask.request.form.get("table-name")
                item_uid = flask.request.form.get("item-uid")


                if table_name.lower() == ("user" or "users"):
                    item = website.models.User.query.filter_by(uid=item_uid).first()
                elif table_name.lower() == ("picture" or "pictures"):
                    item = website.models.Picture.query.filter_by(uid=item_uid).first()
                elif table_name.lower() == ("follow" or "follows"):
                    item = website.models.Follow.query.filter_by(uid=item_uid).first()
                elif table_name.lower() == ("like" or "likes"):
                    item = website.models.Like.query.filter_by(uid=item_uid).first()
                    picture = website.models.Picture.query.filter_by(uid=item.picture_uid).first()


                    picture.likes_count -= 1
                elif table_name.lower() == ("dislike" or "dislikes"):
                    item = website.models.Dislike.query.filter_by(uid=item_uid).first()
                    picture = website.models.Picture.query.filter_by(uid=item.picture_uid).first()


                    picture.dislikes_count -= 1
                elif table_name.lower() == ("comment" or "comments"):
                    item = website.models.Comment.query.filter_by(uid=item_uid).first()
                    picture = website.models.Picture.query.filter_by(uid=item.picture_uid).first()


                    picture.comments_count -= 1
                elif table_name.lower() == ("view" or "views"):
                    item = website.models.View.query.filter_by(uid=item_uid).first()
                    picture = website.models.Picture.query.filter_by(uid=item.picture_uid).first()


                    picture.views_count -= 1


                extensions.db.session.delete(item)
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


            extensions.db.session.commit()


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


@admin.route("/deactivate-user/<user_uid>", methods=["POST"])
@flask_login.login_required
def deactivate_user(user_uid):
    if flask_login.current_user.rank == ("Admin" or "Moderator"):
        try:
            user = website.models.User.query.filter_by(uid=int(user_uid)).first()
            user.status = "inactive"

            extensions.db.session.commit()
        except:
            pass


    return flask.redirect(flask.request.referrer)


@admin.route("/ban-user/<user_uid>", methods=["POST"])
@flask_login.login_required
def ban_user(user_uid):
    if flask_login.current_user.rank == ("Admin" or "Moderator"):
        user = website.models.Picture.query.filter_by(uid=int(user_uid)).first()


        user.status = "banned"

        extensions.db.session.commit()


        flask.flash(
            message = f"Successfully banned the picture #{picture_uid}",
            category = "success"
        )


    return flask.redirect(flask.request.referrer)


@admin.route("/ban-picture/<picture_uid>", methods=["POST"])
@flask_login.login_required
def ban_picture(picture_uid):
    if flask_login.current_user.rank == ("Admin" or "Moderator"):
        picture = website.models.Picture.query.filter_by(uid=int(picture_uid)).first()
        picture_author = website.models.User.query.filter_by(uid=picture.author_uid).first()


        if picture_author.rank != ("Admin" or "Moderator"):
            picture.status = "banned"

            picture_author.karma -= 1

            extensions.db.session.commit()


            flask.flash(
                message = f"Successfully banned the picture #{picture_uid}",
                category = "success"
            )
        else:
            flask.flash(
                message = f"Cannot ban picture #{picture_uid} because its author is the {picture_author.rank}",
                category = "error"
            )



    return flask.redirect(flask.request.referrer)


@admin.route("/ban-comment/<comment_uid>", methods=["POST"])
@flask_login.login_required
def ban_comment(comment_uid):
    if flask_login.current_user.rank == ("Admin" or "Moderator"):
        comment = website.models.Comment.query.filter_by(uid=int(comment_uid)).first()
        comment_author = website.models.User.query.filter_by(uid=comment.author_uid).first()


        if picture_author.rank != ("Admin" or "Moderator"):
            comment.status = "banned"

            comment_author.karma -= 1

            extensions.db.session.commit()


            flask.flash(
                message = f"Successfully banned the comment #{comment_uid}",
                category = "success"
            )
        else:
            flask.flash(
                message = f"Cannot ban comment #{comment_uid} because its author is the {comment_author.rank}",
                category = "error"
            )



    return flask.redirect(flask.request.referrer)

