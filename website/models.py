import datetime

import flask_login

import website


class User(website.db.Model, flask_login.UserMixin):
    id = website.db.Column(
        website.db.Integer,
        primary_key = True
    )
    username = website.db.Column(
        website.db.String,
        unique = True,
        nullable = False
    )
    password = website.db.Column(
        website.db.String,
        nullable = False
    )
    date_created = website.db.Column(
        website.db.DateTime,
        default = datetime.datetime.now(datetime.UTC)
    )
    about_me = website.db.Column(
        website.db.String(),
        default = "Nothing yet..."
    )
    posts = website.db.relationship(
        "Post",
        backref = "user",
        passive_deletes = True
    )
    likes = website.db.relationship(
        "Like",
        backref = "user",
        passive_deletes = True
    )
    comments = website.db.relationship(
        "Comment",
        backref = "user",
        passive_deletes = True
    )


class Post(website.db.Model):
    id = website.db.Column(
        website.db.Integer,
        primary_key = True
    )
    title = website.db.Column(
        website.db.String,
        nullable = False
    )
    image_data = website.db.Column(
        website.db.LargeBinary,
        nullable = False
    )
    date_created = website.db.Column(
        website.db.DateTime(timezone=True),
        default = datetime.datetime.now(datetime.UTC)
    )
    likes = website.db.relationship(
        "Like",
        backref = "post",
        passive_deletes = True
    )
    comments = website.db.relationship(
        "Comment",
        backref = "post",
        passive_deletes = True
    )
    author_id = website.db.Column(
        website.db.Integer,
        website.db.ForeignKey(
            "user.id",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_username = website.db.Column(
        website.db.String,
        nullable = False
    )


class Like(website.db.Model):
    id = website.db.Column(
        website.db.Integer,
        primary_key = True
    )
    date_created = website.db.Column(
        website.db.DateTime(timezone=True),
        default = datetime.datetime.now(datetime.UTC)
    )
    post_id = website.db.Column(
        website.db.Integer,
        website.db.ForeignKey(
            "post.id",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_id = website.db.Column(
        website.db.Integer,
        website.db.ForeignKey(
            "user.id",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_username = website.db.Column(
        website.db.String,
        nullable = False
    )


class Comment(website.db.Model):
    id = website.db.Column(
        website.db.Integer,
        primary_key = True
    )
    text = website.db.Column(
        website.db.String,
        nullable = False
    )
    date_created = website.db.Column(
        website.db.DateTime(timezone=True),
        default = datetime.datetime.now(datetime.UTC)
    )
    post_id = website.db.Column(
        website.db.Integer,
        website.db.ForeignKey(
            "post.id",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_id = website.db.Column(
        website.db.Integer,
        website.db.ForeignKey(
            "user.id",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_username = website.db.Column(
        website.db.String,
        nullable = False
    )
