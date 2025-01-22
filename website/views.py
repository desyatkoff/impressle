import flask

import config


views = flask.Blueprint(
    name = "views",
    import_name = __name__
)


@views.route("/")
def index():
    return flask.render_template(f"{config.PROJECT_ROOT_PATH}/website/templates/index.html")
