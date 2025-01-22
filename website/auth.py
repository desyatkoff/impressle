import flask

import config


auth = flask.Blueprint(
    name = "auth",
    import_name = __name__
)


@auth.route("/signup")
def signup():
    return flask.render_template(f"{config.PROJECT_ROOT_PATH}/website/templates/signup.html")

@auth.route("/login")
def login():
    return flask.render_template(f"{config.PROJECT_ROOT_PATH}/website/templates/login.html")

@auth.route("/logout")
def logout():
    return flask.render_template(f"{config.PROJECT_ROOT_PATH}/website/templates/logout.html")
