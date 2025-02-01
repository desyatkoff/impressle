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
