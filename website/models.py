import datetime

import flask_login

import website


class User(website.db.Model, flask_login.UserMixin):
    id = website.db.Column(
        website.db.Integer,
        primary_key = True
    )

    uid = website.db.Column(
        website.db.Integer,
        unique = True,
        default = lambda: round(datetime.datetime.now(datetime.UTC).timestamp())
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
    rank = website.db.Column(
        website.db.String,
        default = "Newbie"
    )
    xp = website.db.Column(
        website.db.Integer,
        default = 0
    )
    about_me = website.db.Column(
        website.db.String,
        default = "Nothing yet..."
    )
    pictures = website.db.relationship(
        "Picture",
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


class Picture(website.db.Model):
    id = website.db.Column(
        website.db.Integer,
        primary_key = True
    )

    uid = website.db.Column(
        website.db.Integer,
        unique = True,
        default = lambda: round(datetime.datetime.now(datetime.UTC).timestamp())
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
        backref = "picture",
        passive_deletes = True
    )
    comments = website.db.relationship(
        "Comment",
        backref = "picture",
        passive_deletes = True
    )
    author_uid = website.db.Column(
        website.db.Integer,
        website.db.ForeignKey(
            "user.uid",
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

    uid = website.db.Column(
        website.db.Integer,
        unique = True,
        default = lambda: round(datetime.datetime.now(datetime.UTC).timestamp())
    )
    date_created = website.db.Column(
        website.db.DateTime(timezone=True),
        default = datetime.datetime.now(datetime.UTC)
    )
    picture_uid = website.db.Column(
        website.db.Integer,
        website.db.ForeignKey(
            "picture.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_uid = website.db.Column(
        website.db.Integer,
        website.db.ForeignKey(
            "user.uid",
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

    uid = website.db.Column(
        website.db.Integer,
        unique = True,
        default = lambda: round(datetime.datetime.now(datetime.UTC).timestamp())
    )
    text = website.db.Column(
        website.db.String,
        nullable = False
    )
    date_created = website.db.Column(
        website.db.DateTime(timezone=True),
        default = datetime.datetime.now(datetime.UTC)
    )
    picture_uid = website.db.Column(
        website.db.Integer,
        website.db.ForeignKey(
            "picture.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_uid = website.db.Column(
        website.db.Integer,
        website.db.ForeignKey(
            "user.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_username = website.db.Column(
        website.db.String,
        nullable = False
    )
