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


import base64

import flask
import flask_login

import config
import website


views = flask.Blueprint(
    name = "views",
    import_name = __name__
)


@views.before_request
def before_request():
    try:
        user = website.models.User.query.filter_by(uid=flask_login.current_user.uid).first()


        if user.xp > 0:
            user.rank = "Artist"

        if user.xp > 24:
            user.rank = "Amateur Artist"

        if user.xp > 49:
            user.rank = "Cool Guy"

        if user.xp > 99:
            user.rank = "Skilled"

        if user.xp == 666:
            user.rank = "F̷̞́r̴̳͝o̷̥͗m̵̥̚ ̷̧͆t̴͈̍h̷̫͐ȩ̷̂ ̸̰̌H̵̹̆ḙ̶̃l̶̡͝l̸̯̓"

        if user.xp > 999:
            user.rank = "impressive"


        for admin_uid in config.ADMIN_UIDS:
            if user.uid == admin_uid:
                user.rank = "Admin"


        website.db.session.commit()


        if user.is_banned:
            flask_login.logout_user()
            flask.redirect(flask.url_for("views.banned"))
    except:
        pass


@views.route("/")
@views.route("/home")
def index():
    return flask.render_template(
        "index.html",
        user = flask_login.current_user,
        pictures = website.models.Picture.query.all(),
        models = website.models
    )


@views.route("/user/@<username>")
def user_profile(username):
    user = website.models.User.query.filter_by(username=username).first()

    if not user:
        flask.flash(
            message = "Account does not exist",
            category = "error"
        )


        return flask.redirect(flask.request.referrer)


    return flask.render_template(
        "user_profile.html",
        user = flask_login.current_user,
        user_profile = user,
        pictures = website.models.Picture.query.filter_by(
            author_uid = user.uid
        ).all()
    )


@views.route("/settings", methods=["GET", "POST"])
@flask_login.login_required
def user_settings():
    if flask.request.method == "POST":
        user = flask_login.current_user
        about_me_data = flask.request.form.get("about-me")


        if about_me_data is not None:
            flask.flash(
                message = "Successfully saved new settings",
                category = "success"
            )


            user.about_me = about_me_data
            website.db.session.commit()


        return flask.redirect(
            flask.url_for(
                endpoint = "views.user_profile",
                username = user.username
            )
        )


    return flask.render_template(
        "user_settings.html",
        user = flask_login.current_user
    )


@views.route("/create-picture", methods=["GET", "POST"])
@flask_login.login_required
def create_picture():
    if flask.request.method == "POST":
        user = website.models.User.query.filter_by(uid=flask_login.current_user.uid).first()
        image_data = flask.request.form.get("image-data")

        if image_data is not None:
            flask.flash(
                message = "Successfully published your picture",
                category = "success"
            )


            image_binary = base64.b64decode(image_data.split(",")[1])

            picture = website.models.Picture(
                title = flask.request.form.get("title"),
                image_data = image_binary,
                author_uid = flask_login.current_user.uid,
                author_username = flask_login.current_user.username
            )

            user.xp += 1


            website.db.session.add(picture)
            website.db.session.commit()


            return flask.redirect(
                flask.url_for(
                    endpoint = "views.view_picture",
                    picture_uid = picture.uid
                )
            )
        else:
            flask.flash(
                message = "No image data",
                category = "error"
            )


            return flask.redirect(flask.url_for("views.create_picture"))


    return flask.render_template(
        "create_picture.html",
        user = flask_login.current_user
    )


@views.route("/delete-picture/<picture_uid>", methods=["POST"])
@flask_login.login_required
def delete_picture(picture_uid):
    user = website.models.User.query.filter_by(uid=flask_login.current_user.uid).first()
    picture = website.models.Picture.query.filter_by(uid=picture_uid).first()


    if not picture:
        flask.flash(
            message = "Picture does not exist",
            category = "error"
        )
    else:
        if flask_login.current_user.uid == picture.author_uid:
            flask.flash(
                message = "Successfully deleted your picture",
                category = "success"
            )


            user.xp -= 1


            website.db.session.delete(picture)
            website.db.session.commit()
        else:
            flask.flash(
                message = "You do not have enough permissions to delete this picture",
                category = "error"
            )


    return flask.redirect("/")


@views.route("/picture/<picture_uid>")
def view_picture(picture_uid):
    picture = website.models.Picture.query.filter_by(uid=picture_uid).first()


    try:
        view = website.models.View.query.filter_by(author_uid=flask_login.current_user.uid).first()
    except AttributeError:
        view = "Anonymous"


    if not picture:
        flask.flash(
            message = "Picture does not exist",
            category = "error"
        )


        return flask.redirect(flask.request.referrer)
    else:
        if view is None:
            new_view = website.models.View(
                picture_uid = picture_uid,
                author_uid = flask_login.current_user.uid,
                author_username = flask_login.current_user.username
            )


            website.db.session.add(new_view)
            website.db.session.commit()


    return flask.render_template(
        "picture.html",
        user = flask_login.current_user,
        picture = picture,
        models = website.models
    )


@views.route("/about")
def about():
    return flask.render_template(
        "about.html",
        user = flask_login.current_user
    )


@views.route("/faq")
def faq():
    return flask.render_template(
        "faq.html",
        user = flask_login.current_user
    )


@views.route("/banned", methods=["GET", "POST"])
def banned():
    try:
        return flask.redirect(
            flask.url_for(
                "views.user_profile",
                username = flask_login.current_user.username
            )
        )
    except AttributeError:
        if flask.request.method == "POST":
            checkbox = flask.request.form.get("checkbox")


            if checkbox is (False or None):
                flask.flash(
                    "Go away then",
                    category = "warning"
                )
            else:
                return flask.redirect(flask.url_for("auth.signup"))


        return flask.render_template(
            "banned.html",
            user = flask_login.current_user
        )


@views.route("/follow-user/<user_uid>", methods=["POST"])
@flask_login.login_required
def follow_user(user_uid):
    user = website.models.User.query.filter_by(uid=user_uid).first()
    follow = website.models.Follow.query.filter_by(
        followed_uid = user.uid,
        follower_uid = flask_login.current_user.uid
    ).first()


    if not user:
        flask.flash(
            message = "User does not exist",
            category = "error"
        )
    else:
        if follow is None:
            new_follow = website.models.Follow(
                followed_uid = user.uid,
                follower_uid = flask_login.current_user.uid
            )

            website.db.session.add(new_follow)


            user.xp += 1
        else:
            website.db.session.delete(follow)


            user.xp -= 1


        website.db.session.commit()


    return flask.jsonify(
        {
            "followed": flask_login.current_user.uid in map(lambda x: x.follower_uid, user.follows),
            "followers": len(user.follows)
        }
    )


@views.route("/like-picture/<picture_uid>", methods=["POST"])
@flask_login.login_required
def like_picture(picture_uid):
    picture = website.models.Picture.query.filter_by(uid=picture_uid).first()
    like = website.models.Like.query.filter_by(
        picture_uid = picture_uid,
        author_uid = flask_login.current_user.uid,
        author_username = flask_login.current_user.username
    ).first()


    if not picture:
        flask.flash(
            message = "Picture does not exist",
            category = "error"
        )
    else:
        picture_author = website.models.User.query.filter_by(uid=picture.author_uid).first()


        if like:
            website.db.session.delete(like)


            picture_author.xp -= 1
        else:
            like = website.models.Like(
                picture_uid = picture_uid,
                author_uid = flask_login.current_user.uid,
                author_username = flask_login.current_user.username
            )

            website.db.session.add(like)


            picture_author.xp += 1


        website.db.session.commit()


    return flask.jsonify(
        {
            "likes": len(picture.likes),
            "liked": flask_login.current_user.uid in map(lambda x: x.author_uid, picture.likes)
        }
    )


@views.route("/create-comment/<picture_uid>", methods=["POST"])
@flask_login.login_required
def create_comment(picture_uid):
    comment_text = flask.request.form.get("comment-text")
    picture = website.models.Picture.query.filter_by(uid=picture_uid).first()


    if not comment_text:
        flask.flash(
            message = "No comment text",
            category = "error"
        )
    else:
        if picture:
            picture_author = website.models.User.query.filter_by(uid=picture.author_uid).first()


            flask.flash(
                message = "Successfully published your comment",
                category = "success"
            )


            comment = website.models.Comment(
                text = comment_text,
                picture_uid = picture_uid,
                author_uid = flask_login.current_user.uid,
                author_username = flask_login.current_user.username
            )


            website.db.session.add(comment)


            picture_author.xp += 1


            website.db.session.commit()
        else:
            flask.flash(
                message = "Picture does not exist",
                category = "error"
            )


    return flask.redirect(flask.request.referrer)


@views.route("/delete-comment/<comment_uid>", methods=["POST"])
@flask_login.login_required
def delete_comment(comment_uid):
    comment = website.models.Comment.query.filter_by(uid=comment_uid).first()
    picture = website.models.Picture.query.filter_by(uid=comment.picture_uid).first()


    if not comment:
        flask.flash(
            message = "Comment does not exist",
            category = "error"
        )
    else:
        if flask_login.current_user.uid == comment.author_uid:
            picture_author = website.models.User.query.filter_by(uid=picture.author_uid).first()


            flask.flash(
                message = "Successfully deleted your comment",
                category = "success"
            )


            website.db.session.delete(comment)


            picture_author.xp -= 1


            website.db.session.commit()
        else:
            flask.flash(
                message = "You do not have enough permissions to delete this comment",
                category = "error"
            )


    return flask.redirect(flask.request.referrer)
