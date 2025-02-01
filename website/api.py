import flask

import website


api = flask.Blueprint(
    name = "api",
    import_name = __name__
)


@api.route("/get-username-by-uid/<int:user_uid>")
def get_username_by_uid(user_uid):
    user = website.models.User.query.filter_by(uid=user_uid).first()


    if user is not None:
        return website.app.response_class(
            user.username,
            mimetype = "text"
        )


@api.route("/get-picture-by-uid/<int:picture_uid>")
def get_picture_by_uid(picture_uid):
    picture = website.models.Picture.query.filter_by(uid=picture_uid).first()


    if picture is not None:
        return website.app.response_class(
            picture.image_data,
            mimetype = "image/png"
        )


@api.route("/get-comment-text-by-uid/<int:comment_uid>")
def get_comment_text_by_uid(comment_uid):
    comment = website.models.Comment.query.filter_by(uid=comment_uid).first()


    if comment is not None:
        return website.app.response_class(
            comment.text,
            mimetype = "text"
        )
