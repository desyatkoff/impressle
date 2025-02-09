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


import base64
import datetime

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
    if not isinstance(flask_login.current_user, flask_login.AnonymousUserMixin):
        user = website.models.User.query.filter_by(uid=flask_login.current_user.uid).first()


        if user.rank != "Admin":
            if user.karma > 0:
                user.rank = "Artist"

            if user.karma > 24:
                user.rank = "Amateur"

            if user.karma > 49:
                user.rank = "Cool"

            if user.karma > 99:
                user.rank = "Skilled"

            if user.karma == 666:
                user.rank = "F̷̞́r̴̳͝o̷̥͗m̵̥̚ ̷̧͆t̴͈̍h̷̫͐ȩ̷̂ ̸̰̌H̵̹̆ḙ̶̃l̶̡͝l̸̯̓"

            if user.karma > 999:
                user.rank = "Impressive"


        for user_ in website.models.User.query.all():
            if round(datetime.datetime.now(datetime.timezone.utc).timestamp()) - user_.last_activity > 2592000:
                user_.status = "inactive"


        if user.status == "inactive":
            flask_login.logout_user()
            flask.redirect(flask.url_for("views.inactive"))

        if user.status == "banned":
            flask_login.logout_user()
            flask.redirect(flask.url_for("views.banned"))


        user.last_activity = round(datetime.datetime.now(datetime.timezone.utc).timestamp())


        website.db.session.commit()


@views.route("/")
def index():
    return flask.redirect(flask.url_for("views.landing"))


@views.route("/landing")
def landing():
    if isinstance(flask_login.current_user, flask_login.AnonymousUserMixin):
        return flask.render_template(
            "index.html",
            user = flask_login.current_user,
            models = website.models
        )
    else:
        return flask.redirect(
            flask.url_for(
                endpoint = "views.user_profile",
                username = flask_login.current_user.username
            )
        )


@views.route("/feed")
def feed():
    return flask.redirect(flask.url_for("views.feed_recent"))


@views.route("/feed/recent")
def feed_recent():
    recent_pictures = website.models.Picture.query.order_by(
        website.models.Picture.uid.desc()
    ).order_by(
        website.models.Picture.likes_count.desc()
    ).order_by(
        website.models.Picture.dislikes_count.asc()
    ).order_by(
        website.models.Picture.views_count.desc()
    ).all()


    return flask.render_template(
        "feed.html",
        user = flask_login.current_user,
        pictures = recent_pictures,
        feed_type = "recent",
        models = website.models
    )


@views.route("/feed/best")
def feed_best():
    best_pictures = website.models.Picture.query.order_by(
        website.models.Picture.likes_count.desc()
    ).order_by(
        website.models.Picture.dislikes_count.asc()
    ).order_by(
        website.models.Picture.views_count.desc()
    ).order_by(
        website.models.Picture.uid.desc()
    ).all()


    return flask.render_template(
        "feed.html",
        user = flask_login.current_user,
        pictures = best_pictures,
        feed_type = "best",
        models = website.models
    )


@views.route("/feed/popular")
def feed_popular():
    popular_pictures = website.models.Picture.query.order_by(
        website.models.Picture.views_count.desc()
    ).order_by(
        website.models.Picture.likes_count.desc()
    ).order_by(
        website.models.Picture.dislikes_count.asc()
    ).order_by(
        website.models.Picture.uid.desc()
    ).all()


    return flask.render_template(
        "feed.html",
        user = flask_login.current_user,
        pictures = popular_pictures,
        feed_type = "popular",
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


        return flask.redirect(flask.url_for("views.feed"))


    return flask.render_template(
        "user_profile.html",
        user = flask_login.current_user,
        user_profile = user,
        pictures = website.models.Picture.query.filter_by(
            author_uid = user.uid
        ).all(),
        models = website.models
    )


@views.route("/settings", methods=["GET", "POST"])
@flask_login.login_required
def user_settings():
    if flask.request.method == "POST":
        user = flask_login.current_user

        about_me_data = flask.request.form.get("about-me")
        show_followers_data = flask.request.form.get("show-followers-checkbox")
        allow_comments_data = flask.request.form.get("allow-comments-checkbox")
        delete_account_data = flask.request.form.get("delete-account-checkbox")


        user.about_me = about_me_data
        user.show_followers = True if show_followers_data == "on" else False
        user.allow_comments = True if allow_comments_data == "on" else False
        user.status = "inactive" if delete_account_data == "on" else "normal"


        flask.flash(
            message = "Successfully saved new settings",
            category = "success"
        )


        website.db.session.commit()


        return flask.redirect(
            flask.url_for(
                endpoint = "views.user_profile",
                username = user.username
            )
        )


    return flask.render_template(
        "user_settings.html",
        user = flask_login.current_user,
        models = website.models
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

            user.karma += 1


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
        user = flask_login.current_user,
        models = website.models
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


            picture.status = "deleted"


            user.karma -= 1


            website.db.session.commit()
        else:
            flask.flash(
                message = "You do not have enough permissions to delete this picture",
                category = "error"
            )


    return flask.redirect(flask.url_for("views.feed"))


@views.route("/picture/<picture_uid>")
def view_picture(picture_uid):
    picture = website.models.Picture.query.filter_by(uid=picture_uid).first()
    user = flask_login.current_user


    if not isinstance(user, flask_login.AnonymousUserMixin):
        view = website.models.View.query.filter_by(author_uid=user.uid).first()
    else:
        view = ""


    if not picture:
        flask.flash(
            message = "Picture does not exist",
            category = "error"
        )


        return flask.redirect(flask.url_for("views.feed"))
    else:
        if view is None:
            new_view = website.models.View(
                picture_uid = picture_uid,
                author_uid = flask_login.current_user.uid,
                author_username = flask_login.current_user.username
            )

            picture.views_count += 1


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
        user = flask_login.current_user,
        models = website.models
    )


@views.route("/faq")
def faq():
    return flask.render_template(
        "faq.html",
        user = flask_login.current_user,
        models = website.models
    )


@views.route("/terms-of-service")
def terms_of_service():
    return flask.render_template(
        "terms_of_service.html",
        user = flask_login.current_user,
        models = website.models
    )


@views.route("/privacy-policy")
def privacy_policy():
    return flask.render_template(
        "privacy_policy.html",
        user = flask_login.current_user,
        models = website.models
    )


@views.route("/inactive")
def inactive():
    try:
        return flask.render_template(
            "inactive.html",
            user = flask_login.current_user
        )
    except:
        pass


@views.route("/banned", methods=["GET", "POST"])
def banned():
    try:
        if flask.request.method == "POST":
            checkbox = flask.request.form.get("checkbox")


            if checkbox != "on":
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
    except:
        pass


@views.route("/follow-user/<user_uid>", methods=["POST"])
@flask_login.login_required
def follow_user(user_uid):
    user = website.models.User.query.filter_by(uid=user_uid).first()
    follow = website.models.Follow.query.filter_by(
        followed_uid = user.uid,
        followed_username = user.username,
        follower_uid = flask_login.current_user.uid,
        follower_username = flask_login.current_user.username
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
                followed_username = user.username,
                follower_uid = flask_login.current_user.uid,
                follower_username = flask_login.current_user.username
            )

            website.db.session.add(new_follow)


            user.karma += 1
        else:
            website.db.session.delete(follow)


            user.karma -= 1


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
    dislike = website.models.Dislike.query.filter_by(
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

            picture.likes_count -= 1


            picture_author.karma -= 1
        else:
            like = website.models.Like(
                picture_uid = picture_uid,
                author_uid = flask_login.current_user.uid,
                author_username = flask_login.current_user.username
            )

            website.db.session.add(like)

            picture.likes_count += 1


            picture_author.karma += 1


            if dislike:
                website.db.session.delete(dislike)

                picture.dislikes_count -= 1

                picture_author.karma += 1


        website.db.session.commit()


    return flask.jsonify(
        {
            "likes": len(picture.likes),
            "liked": flask_login.current_user.uid in map(lambda x: x.author_uid, picture.likes),
            "dislikes": len(picture.dislikes),
            "disliked": flask_login.current_user.uid in map(lambda x: x.author_uid, picture.dislikes)
        }
    )


@views.route("/dislike-picture/<picture_uid>", methods=["POST"])
@flask_login.login_required
def dislike_picture(picture_uid):
    picture = website.models.Picture.query.filter_by(uid=picture_uid).first()
    like = website.models.Like.query.filter_by(
        picture_uid = picture_uid,
        author_uid = flask_login.current_user.uid,
        author_username = flask_login.current_user.username
    ).first()
    dislike = website.models.Dislike.query.filter_by(
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


        if dislike:
            website.db.session.delete(dislike)

            picture.dislikes_count -= 1


            picture_author.karma += 1
        else:
            dislike = website.models.Dislike(
                picture_uid = picture_uid,
                author_uid = flask_login.current_user.uid,
                author_username = flask_login.current_user.username
            )

            website.db.session.add(dislike)

            picture.dislikes_count += 1


            picture_author.karma -= 1


            if like:
                website.db.session.delete(like)

                picture.likes_count -= 1

                picture_author.karma -= 1


        website.db.session.commit()


    return flask.jsonify(
        {
            "likes": len(picture.likes),
            "liked": flask_login.current_user.uid in map(lambda a: a.author_uid, picture.likes),
            "dislikes": len(picture.dislikes),
            "disliked": flask_login.current_user.uid in map(lambda b: b.author_uid, picture.dislikes)
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


            picture_author.karma += 1


            website.db.session.commit()
        else:
            flask.flash(
                message = "Picture does not exist",
                category = "error"
            )


    return flask.redirect(flask.url_for("views.feed"))


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


            comment.status = "deleted"


            picture_author.karma -= 1


            website.db.session.commit()
        else:
            flask.flash(
                message = "You do not have enough permissions to delete this comment",
                category = "error"
            )


    return flask.redirect(flask.url_for("views.feed"))
