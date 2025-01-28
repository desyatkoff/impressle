import base64

import flask
import flask_login

import website


views = flask.Blueprint(
    name = "views",
    import_name = __name__
)


@views.route("/")
@views.route("/home")
def index():
    return flask.render_template(
        "index.html",
        user = flask_login.current_user,
        posts = website.models.Post.query.all()
    )


@views.route("/user/@<username>")
def user_profile(username):
    user = website.models.User.query.filter_by(username=username).first()

    if not user:
        flask.flash(
            message = "Account does not exist",
            category = "error"
        )


        return flask.redirect(flask.url_for("views.index"))


    return flask.render_template(
        "user_profile.html",
        user = flask_login.current_user,
        user_profile = user,
        posts = website.models.Post.query.filter_by(
            author_id = user.id
        ).all()
    )


@views.route("/settings", methods=["GET", "POST"])
@flask_login.login_required
def user_settings():
    if flask.request.method == "POST":
        user = flask_login.current_user
        about_me_data = flask.request.form.get("about_me")

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
        else:
            flask.flash(
                message = "No any data",
                category = "error"
            )


    return flask.render_template(
        "user_settings.html",
        user = flask_login.current_user
    )


@views.route("/create-post", methods=["GET", "POST"])
@flask_login.login_required
def create_post():
    if flask.request.method == "POST":
        image_data = flask.request.form.get("image_data")

        if image_data is not None:
            flask.flash(
                message = "Successfully published your post",
                category = "success"
            )


            image_binary = base64.b64decode(image_data.split(",")[1])

            post = website.models.Post(
                title = flask.request.form.get("title"),
                image_data = image_binary,
                author_id = flask_login.current_user.id,
                author_username = flask_login.current_user.username
            )


            website.db.session.add(post)
            website.db.session.commit()


            return flask.redirect(flask.url_for("views.index"))
        else:
            flask.flash(
                message = "No image data",
                category = "error"
            )


            return flask.redirect(flask.url_for("views.create_post"))


    return flask.render_template(
        "create_post.html",
        user = flask_login.current_user
    )


@views.route("/like-post/<post_id>", methods=["POST"])
@flask_login.login_required
def like_post(post_id):
    post = website.models.Post.query.filter_by(id=post_id).first()
    like = website.models.Like.query.filter_by(
        post_id = post_id,
        author_id = flask_login.current_user.id,
        author_username = flask_login.current_user.username
    ).first()


    if not post:
        flask.flash(
            message = "Post does not exist",
            category = "error"
        )
    else:
        if like:
            website.db.session.delete(like)
        else:
            like = website.models.Like(
                post_id = post_id,
                author_id = flask_login.current_user.id,
                author_username = flask_login.current_user.username
            )

            website.db.session.add(like)

        website.db.session.commit()


    return flask.jsonify(
        {
            "likes": len(post.likes),
            "liked": flask_login.current_user.id in map(lambda x: x.author_id, post.likes)
        }
    )
