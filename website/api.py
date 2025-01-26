import flask

import website


api = flask.Blueprint(
    name = "api",
    import_name = __name__
)


@api.route("/get-username-by-id/id=<user_id>")
def get_username_by_id(user_id):
    user = website.models.User.query.get(user_id)


    if user is not None:
        return website.app.response_class(
            user.username,
            mimetype = "text"
        )


@api.route("/get-post-image-by-id/id=<post_id>")
def get_post_image_by_id(post_id):
    post = website.models.Post.query.get(post_id)


    if post is not None:
        return website.app.response_class(
            post.image_data,
            mimetype = "image/png"
        )


@api.route("/get-comment-text-by-id/id=<comment_id>")
def get_comment_text_by_id(comment_id):
    comment = website.models.Comment.query.get(comment_id)


    if comment is not None:
        return website.app.response_class(
            comment.text,
            mimetype = "text"
        )
