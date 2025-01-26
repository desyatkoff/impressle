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
    return flask.render_template("index.html", user=flask_login.current_user, posts=website.models.Post.query.all())


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
        username = username,
        posts = website.models.Post.query.filter_by(
            author_username = username
        ).all()
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


    return flask.render_template("create_post.html", user=flask_login.current_user)
