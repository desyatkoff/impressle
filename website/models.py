import datetime

import flask_login

import website


class User(website.db.Model, flask_login.UserMixin):
    id = website.db.Column(
        website.db.Integer,
        primary_key = True
    )
    username = website.db.Column(
        website.db.String(32),
        unique = True,
        nullable = False
    )
    password = website.db.Column(
        website.db.String(256),
        nullable = False
    )
    joining_date = website.db.Column(
        website.db.DateTime(timezone=True),
        default = datetime.datetime.now(datetime.UTC)
    )
    is_banned = website.db.Column(
        website.db.Boolean,
        default = False
    )
