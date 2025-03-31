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


import io
import base64
import difflib
import datetime

import flask
import flask_login

import website
from . import extensions


routes = flask.Blueprint(
    name = "routes",
    import_name = __name__
)


@routes.before_request
def before_request():
    if not isinstance(flask_login.current_user, flask_login.AnonymousUserMixin):
        user = website.models.User.query.filter_by(uid=flask_login.current_user.uid).first() 


        for user_ in website.models.User.query.all():
            # If user is not an admin or a moderator,
            # set their rank to something
            if user_.rank != ("Admin" or "Moderator"):
                if user_.karma > 0:
                    user_.rank = "Artist"

                if user_.karma > 24:
                    user_.rank = "Amateur"

                if user_.karma > 49:
                    user_.rank = "Cool"

                if user_.karma > 99:
                    user_.rank = "Skilled"

                if user_.karma == 666:
                    user_.rank = "F̷̞́r̴̳͝o̷̥͗m̵̥̚ ̷̧͆t̴͈̍h̷̫͐ȩ̷̂ ̸̰̌H̵̹̆ḙ̶̃l̶̡͝l̸̯̓"

                if user_.karma > 999:
                    user_.rank = "Impressive"


            # If user's last activity was more than a month ago,
            # set their status to "inactive"
            if round(
                    datetime.datetime.now(
                        tz = datetime.timezone.utc
                    ).timestamp()
                ) - user_.last_activity > 2592000:    # 259200 seconds = 30 days
                if user_.status != "banned":
                    user_.status = "inactive"


            # If user's last activity was
            # - [0-10] seconds ago -> set their status to "online"
            # - More than 10 seconds ago -> set their status to "offline"
            if round(
                    datetime.datetime.now(
                        tz = datetime.timezone.utc
                    ).timestamp()
                ) - user_.last_activity <= 10:
                if user_.status == "offline":
                    user_.status = "online"
            else:
                if user_.status == "online":
                    user_.status = "offline"


        if user.status == "inactive":
            flask_login.logout_user()
            flask.redirect(flask.url_for("routes.inactive"))

        if user.status == "banned":
            flask_login.logout_user()
            flask.redirect(flask.url_for("routes.banned"))


        user.last_activity = round(
            datetime.datetime.now(
                tz = datetime.timezone.utc
            ).timestamp()
        )


        extensions.db.session.commit()


@routes.route("/")
def index():
    return flask.redirect(flask.url_for("routes.landing"))


@routes.route("/landing")
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
                endpoint = "routes.user_profile",
                username = flask_login.current_user.username
            )
        )


@routes.route("/search-picture/<query>")
def search_picture(query):
    pictures = website.models.Picture.query.order_by(
        website.models.Picture.uid.desc()
    ).order_by(
        website.models.Picture.likes_count.desc()
    ).order_by(
        website.models.Picture.dislikes_count.asc()
    ).order_by(
        website.models.Picture.views_count.desc()
    ).all()
    relevant_pictures = []


    for picture in pictures:
        if difflib.SequenceMatcher(
            a = str(query).lower(),
            b = str(picture.title).lower()
        ).ratio() > 0.5 or query == picture.uid:
            relevant_pictures.append(picture)


    return flask.render_template(
        "search.html",
        user = flask_login.current_user,
        pictures = relevant_pictures,
        models = website.models
    )


@routes.route("/feed")
def feed():
    return flask.redirect(flask.url_for("routes.feed_recent"))


@routes.route("/feed/recent")
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


@routes.route("/feed/best")
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


@routes.route("/feed/popular")
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


@routes.route("/user")
@flask_login.login_required
def current_user_profile():
    return flask.redirect(
        flask.url_for(
            endpoint = "routes.user_profile",
            username = flask_login.current_user.username
        )
    )


@routes.route("/user/@<username>")
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
        ).order_by(
            website.models.Picture.uid.desc()
        ).order_by(
            website.models.Picture.likes_count.desc()
        ).order_by(
            website.models.Picture.dislikes_count.asc()
        ).order_by(
            website.models.Picture.views_count.desc()
        ).all(),
        models = website.models
    )


@routes.route("/settings", methods=["GET", "POST"])
@flask_login.login_required
def user_settings():
    if flask.request.method == "POST":
        user = flask_login.current_user

        about_me_data = flask.request.form.get("about-me")
        show_followers_data = flask.request.form.get("show-followers-checkbox")
        allow_comments_data = flask.request.form.get("allow-comments-checkbox")
        show_status_data = flask.request.form.get("show-status-checkbox")
        delete_account_data = flask.request.form.get("delete-account-checkbox")


        if len(about_me_data) > 64:
            flask.flash(
                message = "\"About Me\" is too long",
                category = "error"
            )
        else:
            user.about_me = about_me_data

        if show_followers_data == "on":
            user.show_followers = True
        else:
            user.show_followers = False

        if allow_comments_data == "on":
            user.allow_comments = True
        else:
            user.allow_comments = False

        if show_status_data == "on":
            user.show_status = True
        else:
            user.show_status = False

        if delete_account_data == "on":
            user.status = "inactive"


        flask.flash(
            message = "Successfully saved new settings",
            category = "success"
        )


        extensions.db.session.commit()


        return flask.redirect(
            flask.url_for(
                endpoint = "routes.user_profile",
                username = user.username
            )
        )


    return flask.render_template(
        "user_settings.html",
        user = flask_login.current_user,
        models = website.models
    )


@routes.route("/create-picture", methods=["GET", "POST"])
@flask_login.login_required
def create_picture():
    if flask.request.method == "POST":
        user = flask_login.current_user
        title = flask.request.form.get("title")
        description = flask.request.form.get("description")
        image_data = flask.request.form.get("image-data")

        if image_data is not None:
            if len(title) > 100:
                flask.flash(
                    message = "Picture title is too long",
                    category = "error"
                )


                return flask.redirect(flask.url_for("routes.create_picture"))
            elif len(description) > 100:
                flask.flash(
                    message = "Picture description is too long",
                    category = "error"
                )


                return flask.redirect(flask.url_for("routes.create_picture"))
            else:
                flask.flash(
                    message = "Successfully published your picture",
                    category = "success"
                )


                image_binary = base64.b64decode(image_data.split(",")[1])

                picture = website.models.Picture(
                    title = title,
                    description = description,
                    image_data = image_binary,
                    author_uid = user.uid,
                    author_username = user.username
                )

                user.karma += 1


                extensions.db.session.add(picture)
                extensions.db.session.commit()


                return flask.redirect(
                    flask.url_for(
                        endpoint = "routes.full_view_picture",
                        picture_uid = picture.uid
                    )
                )
        else:
            flask.flash(
                message = "No image data",
                category = "error"
            )


            return flask.redirect(flask.url_for("routes.create_picture"))


    return flask.render_template(
        "create_picture.html",
        user = flask_login.current_user,
        models = website.models
    )


@routes.route("/liked")
@flask_login.login_required
def liked():
    pictures = website.models.Picture.query.order_by(
        website.models.Picture.uid.desc()
    ).order_by(
        website.models.Picture.likes_count.desc()
    ).order_by(
        website.models.Picture.dislikes_count.asc()
    ).order_by(
        website.models.Picture.views_count.desc()
    ).all()


    return flask.render_template(
        "liked.html",
        user = flask_login.current_user,
        pictures = pictures,
        models = website.models
    )


@routes.route("/following")
@flask_login.login_required
def following():
    users = website.models.User.query.order_by(
        website.models.User.uid.desc()
    ).all()


    return flask.render_template(
        "following.html",
        user = flask_login.current_user,
        users = users,
        models = website.models
    )


@routes.route("/delete-picture/<picture_uid>", methods=["POST"])
@flask_login.login_required
def delete_picture(picture_uid):
    user = flask_login.current_user
    picture = website.models.Picture.query.filter_by(uid=picture_uid).first()


    if not picture:
        flask.flash(
            message = "Picture does not exist",
            category = "error"
        )
    else:
        if user.uid == picture.author_uid or user.rank == "Admin":
            flask.flash(
                message = "Successfully deleted your picture",
                category = "success"
            )


            picture.status = "deleted"


            user.karma -= 1


            extensions.db.session.commit()
        else:
            flask.flash(
                message = "You do not have enough permissions to delete this picture",
                category = "error"
            )


    return flask.redirect(flask.url_for("routes.feed"))


@routes.route("/picture/<picture_uid>")
def full_view_picture(picture_uid):
    picture = website.models.Picture.query.filter_by(uid=picture_uid).first()
    comments = website.models.Comment.query.filter_by(
        picture_uid = picture_uid
    ).order_by(
        website.models.Comment.uid.desc()
    ).all()
    user = flask_login.current_user


    if not isinstance(user, flask_login.AnonymousUserMixin):
        view = website.models.View.query.filter_by(
            author_uid = user.uid,
            picture_uid = picture_uid
        ).first()
    else:
        view = ""


    if not picture or picture.status == "deleted":
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

            picture.views_count += 1


            extensions.db.session.add(new_view)
            extensions.db.session.commit()


    return flask.render_template(
        "picture.html",
        user = flask_login.current_user,
        picture = picture,
        comments = comments,
        models = website.models
    )


@routes.route("/about")
def about():
    return flask.render_template(
        "about.html",
        user = flask_login.current_user,
        models = website.models
    )


@routes.route("/faq")
def faq():
    return flask.render_template(
        "faq.html",
        user = flask_login.current_user,
        models = website.models
    )


@routes.route("/terms-of-service")
def terms_of_service():
    return flask.render_template(
        "terms_of_service.html",
        user = flask_login.current_user,
        models = website.models
    )


@routes.route("/privacy-policy")
def privacy_policy():
    return flask.render_template(
        "privacy_policy.html",
        user = flask_login.current_user,
        models = website.models
    )


@routes.route("/inactive")
def inactive():
    try:
        return flask.render_template(
            "inactive.html",
            user = flask_login.current_user
        )
    except:
        pass


@routes.route("/banned", methods=["GET", "POST"])
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


@routes.route("/follow-user/<user_uid>", methods=["POST"])
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

            extensions.db.session.add(new_follow)


            user.karma += 1
        else:
            extensions.db.session.delete(follow)


            user.karma -= 1


        extensions.db.session.commit()


    return flask.jsonify(
        {
            "followed": flask_login.current_user.uid in map(lambda x: x.follower_uid, user.follows),
            "followers": len(user.follows)
        }
    )


@routes.route("/view-picture/<picture_uid>", methods=["POST"])
@flask_login.login_required
def view_picture(picture_uid):
    picture = website.models.Picture.query.filter_by(uid=picture_uid).first()
    picture_author = website.models.User.query.filter_by(uid=picture.author_uid).first()
    view = website.models.View.query.filter_by(
        author_uid = flask_login.current_user.uid,
        picture_uid = picture.uid
    ).first()


    if not picture:
        flask.flash(
            message = "Picture does not exist",
            category = "error"
        )
    else:
        if view is None:
            new_view = website.models.View(
                picture_uid = picture.uid,
                author_uid = flask_login.current_user.uid,
                author_username = flask_login.current_user.username
            )

            picture.views_count += 1


            extensions.db.session.add(new_view)


        extensions.db.session.commit()


    return flask.jsonify(
        {
            "views": picture.views_count,
            "viewed": flask_login.current_user.uid in map(lambda x: x.author_uid, picture.views)
        }
    )


@routes.route("/like-picture/<picture_uid>", methods=["POST"])
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
            extensions.db.session.delete(like)

            picture.likes_count -= 1


            picture_author.karma -= 1
        else:
            if flask_login.current_user != picture_author:
                like = website.models.Like(
                    picture_uid = picture_uid,
                    author_uid = flask_login.current_user.uid,
                    author_username = flask_login.current_user.username
                )

                extensions.db.session.add(like)

                picture.likes_count += 1


                picture_author.karma += 1


                if dislike:
                    extensions.db.session.delete(dislike)

                    picture.dislikes_count -= 1

                    picture_author.karma += 1


        view = website.models.View.query.filter_by(
            author_uid = flask_login.current_user.uid,
            picture_uid = picture.uid
        ).first()


        if view is None:
            new_view = website.models.View(
                picture_uid = picture.uid,
                author_uid = flask_login.current_user.uid,
                author_username = flask_login.current_user.username
            )

            picture.views_count += 1


            extensions.db.session.add(new_view)


        extensions.db.session.commit()


    return flask.jsonify(
        {
            "likes": len(picture.likes),
            "liked": flask_login.current_user.uid in map(lambda x: x.author_uid, picture.likes),
            "dislikes": len(picture.dislikes),
            "disliked": flask_login.current_user.uid in map(lambda x: x.author_uid, picture.dislikes)
        }
    )


@routes.route("/dislike-picture/<picture_uid>", methods=["POST"])
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
            extensions.db.session.delete(dislike)

            picture.dislikes_count -= 1


            picture_author.karma += 1
        else:
            if flask_login.current_user != picture_author:
                dislike = website.models.Dislike(
                    picture_uid = picture_uid,
                    author_uid = flask_login.current_user.uid,
                    author_username = flask_login.current_user.username
                )

                extensions.db.session.add(dislike)

                picture.dislikes_count += 1


                picture_author.karma -= 1


                if like:
                    extensions.db.session.delete(like)

                    picture.likes_count -= 1

                    picture_author.karma -= 1


        view = website.models.View.query.filter_by(
            author_uid = flask_login.current_user.uid,
            picture_uid = picture.uid
        ).first()


        if view is None:
            new_view = website.models.View(
                picture_uid = picture.uid,
                author_uid = flask_login.current_user.uid,
                author_username = flask_login.current_user.username
            )

            picture.views_count += 1


            extensions.db.session.add(new_view)


        extensions.db.session.commit()


    return flask.jsonify(
        {
            "likes": len(picture.likes),
            "liked": flask_login.current_user.uid in map(lambda a: a.author_uid, picture.likes),
            "dislikes": len(picture.dislikes),
            "disliked": flask_login.current_user.uid in map(lambda b: b.author_uid, picture.dislikes)
        }
    )


@routes.route("/download-picture/<picture_uid>")
def download_picture(picture_uid):
    picture = website.models.Picture.query.filter_by(uid=picture_uid).first()
    picture_author = website.models.User.query.filter_by(uid=picture.author_uid).first()

    if not isinstance(flask_login.current_user, flask_login.AnonymousUserMixin):
        dl_author = flask_login.current_user
        download = website.models.Download.query.filter_by(
            author_uid = flask_login.current_user.uid,
            picture_uid = picture.uid
        ).first()
    else:
        dl_author = None 
        download = None


    if not picture:
        flask.flash(
            message = "Picture does not exist",
            category = "error"
        )
    else:
        flask.flash(
            message = f"Successfully downloaded the picture #{picture_uid}",
            category = "success"
        ) 


        if dl_author is not None and download is None:
            new_download = website.models.Download(
                picture_uid = picture.uid,
                author_uid = flask_login.current_user.uid,
                author_username = flask_login.current_user.username
            )

            picture.downloads_count += 1


            extensions.db.session.add(new_download)
            extensions.db.session.commit()


        return flask.send_file(
            path_or_file = io.BytesIO(picture.image_data), 
            as_attachment = True,
            download_name = f"{picture_uid}.png"
        ) 

    
    return flask.jsonify(
        {
            "downloads": picture.downloads_count
        }
    )


@routes.route("/create-comment/<picture_uid>", methods=["POST"])
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

            picture.comments_count += 1


            extensions.db.session.add(comment)


            picture_author.karma += 1


            extensions.db.session.commit()
        else:
            flask.flash(
                message = "Picture does not exist",
                category = "error"
            )


    return flask.redirect(
        flask.url_for(
            endpoint = "routes.full_view_picture",
            picture_uid = picture_uid
        )
    )


@routes.route("/delete-comment/<comment_uid>", methods=["POST"])
@flask_login.login_required
def delete_comment(comment_uid):
    user = flask_login.current_user
    comment = website.models.Comment.query.filter_by(uid=comment_uid).first()
    picture = website.models.Picture.query.filter_by(uid=comment.picture_uid).first()


    if not comment:
        flask.flash(
            message = "Comment does not exist",
            category = "error"
        )
    else:
        if user.uid == comment.author_uid or user.rank == "Admin":
            picture_author = website.models.User.query.filter_by(uid=picture.author_uid).first()


            flask.flash(
                message = "Successfully deleted your comment",
                category = "success"
            )


            comment.status = "deleted"

            picture.comments_count -= 1


            picture_author.karma -= 1


            extensions.db.session.commit()
        else:
            flask.flash(
                message = "You do not have enough permissions to delete this comment",
                category = "error"
            )


    return flask.redirect(
        flask.url_for(
            endpoint = "routes.full_view_picture",
            picture_uid = picture.uid
        )
    )
