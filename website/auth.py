import flask
import flask_login
import werkzeug

import website


auth = flask.Blueprint(
    name = "auth",
    import_name = __name__
)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "POST":
        username = flask.request.form.get("username")
        password = flask.request.form.get("password")


        if website.models.User.query.filter_by(username=username).first() is not None:
            flask.flash(
                message = "Username is already taken",
                category = "error"
            )
        elif len(username) < 4:
            flask.flash(
                message = "Username is too short",
                category = "error"
            )
        elif len(password) < 8:
            flask.flash(
                message = "Password is too short",
                category = "error"
            )
        else:
            flask.flash(
                message = "Successfully created new account",
                category = "success"
            )


            new_user = website.models.User(
                username = username,
                password = werkzeug.security.generate_password_hash(
                    password = password,
                    method = "scrypt"
                )
            )


            website.db.session.add(new_user)
            website.db.session.commit()


            flask_login.login_user(
                user = new_user,
                remember = True
            )


            return flask.redirect(f"/user/@{new_user.username}")


    return flask.render_template("signup.html", user=flask_login.current_user)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "POST":
        username = flask.request.form.get("username")
        password = flask.request.form.get("password")

        user = website.models.User.query.filter_by(username=username).first()


        if user is not None:
            if werkzeug.security.check_password_hash(user.password, password):
                flask.flash(
                    message = "Successfully logged in",
                    category = "success"
                )

                flask_login.login_user(
                    user = user,
                    remember = True
                )


                return flask.redirect(f"/user/@{user.username}")
            else:
                flask.flash(
                    message = "Invalid password",
                    category = "error"
                )
        else:
            flask.flash(
                message = "Account does not exist",
                category = "error"
            )


    return flask.render_template("login.html", user=flask_login.current_user)


@auth.route("/logout")
@flask_login.login_required
def logout():
    flask.flash(
        message = "Successfully logget out",
        category = "success"
    )


    flask_login.logout_user()


    return flask.redirect(flask.url_for("auth.login"))
