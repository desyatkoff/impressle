#!usr/bin/env python3
#
# Copyright (C) 2025 Desyatkov Sergey
#
# This file is part of Impressle.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.


import datetime

import flask_login

from . import extensions


class User(extensions.db.Model, flask_login.UserMixin):
    id = extensions.db.Column(
        extensions.db.Integer,
        primary_key = True,
        nullable = False
    )

    uid = extensions.db.Column(
        extensions.db.Integer,
        unique = True,
        default = lambda: round(datetime.datetime.now(datetime.timezone.utc).timestamp())
    )
    date_created = extensions.db.Column(
        extensions.db.DateTime,
        default = datetime.datetime.now(datetime.timezone.utc)
    )
    username = extensions.db.Column(
        extensions.db.String,
        unique = True,
        nullable = False
    )
    password = extensions.db.Column(
        extensions.db.String,
        nullable = False
    )
    about_me = extensions.db.Column(
        extensions.db.String
    )
    karma = extensions.db.Column(
        extensions.db.Integer,
        default = 0
    )
    rank = extensions.db.Column(
        extensions.db.String,
        default = "Newbie"
    )
    pictures = extensions.db.relationship(
        "Picture",
        backref = "user",
        passive_deletes = True
    )
    follows = extensions.db.relationship(
        "Follow",
        backref = "user",
        passive_deletes = True
    )
    likes = extensions.db.relationship(
        "Like",
        backref = "user",
        passive_deletes = True
    )
    comments = extensions.db.relationship(
        "Comment",
        backref = "user",
        passive_deletes = True
    )
    show_followers = extensions.db.Column(
        extensions.db.Boolean,
        default = True
    )
    allow_comments = extensions.db.Column(
        extensions.db.Boolean,
        default = True
    )
    status = extensions.db.Column(
        extensions.db.String,
        default = "normal"
    )
    last_activity = extensions.db.Column(
        extensions.db.Integer,
        default = lambda: round(datetime.datetime.now(datetime.timezone.utc).timestamp())
    )


class Picture(extensions.db.Model):
    id = extensions.db.Column(
        extensions.db.Integer,
        primary_key = True,
        nullable = False
    )

    uid = extensions.db.Column(
        extensions.db.Integer,
        unique = True,
        default = lambda: round(datetime.datetime.now(datetime.timezone.utc).timestamp())
    )
    date_created = extensions.db.Column(
        extensions.db.DateTime(timezone=True),
        default = datetime.datetime.now(datetime.timezone.utc)
    )
    title = extensions.db.Column(
        extensions.db.String,
        nullable = False
    )
    image_data = extensions.db.Column(
        extensions.db.LargeBinary,
        nullable = False
    )
    likes = extensions.db.relationship(
        "Like",
        backref = "picture",
        passive_deletes = True
    )
    likes_count = extensions.db.Column(
        extensions.db.Integer,
        default = 0
    )
    dislikes = extensions.db.relationship(
        "Dislike",
        backref = "picture",
        passive_deletes = True
    )
    dislikes_count = extensions.db.Column(
        extensions.db.Integer,
        default = 0
    )
    comments = extensions.db.relationship(
        "Comment",
        backref = "picture",
        passive_deletes = True
    )
    comments_count = extensions.db.Column(
        extensions.db.Integer,
        default = 0
    )
    views = extensions.db.relationship(
        "View",
        backref = "picture",
        passive_deletes = True
    )
    views_count = extensions.db.Column(
        extensions.db.Integer,
        default = 0
    )
    author_uid = extensions.db.Column(
        extensions.db.Integer,
        extensions.db.ForeignKey(
            "user.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_username = extensions.db.Column(
        extensions.db.String,
        nullable = False
    )
    status = extensions.db.Column(
        extensions.db.String,
        default = "normal"
    )


class Follow(extensions.db.Model):
    id = extensions.db.Column(
        extensions.db.Integer,
        primary_key = True,
        nullable = False
    )

    uid = extensions.db.Column(
        extensions.db.Integer,
        unique = True,
        default = lambda: round(datetime.datetime.now(datetime.timezone.utc).timestamp())
    )
    date_created = extensions.db.Column(
        extensions.db.DateTime(timezone=True),
        default = datetime.datetime.now(datetime.timezone.utc)
    )
    followed_uid = extensions.db.Column(
        extensions.db.Integer,
        extensions.db.ForeignKey(
            "user.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    followed_username = extensions.db.Column(
        extensions.db.String,
        nullable = False
    )
    follower_uid = extensions.db.Column(
        extensions.db.Integer,
        nullable = False
    )
    follower_username = extensions.db.Column(
        extensions.db.String,
        nullable = False
    )


class Like(extensions.db.Model):
    id = extensions.db.Column(
        extensions.db.Integer,
        primary_key = True,
        nullable = False
    )

    uid = extensions.db.Column(
        extensions.db.Integer,
        unique = True,
        default = lambda: round(datetime.datetime.now(datetime.timezone.utc).timestamp())
    )
    date_created = extensions.db.Column(
        extensions.db.DateTime(timezone=True),
        default = datetime.datetime.now(datetime.timezone.utc)
    )
    picture_uid = extensions.db.Column(
        extensions.db.Integer,
        extensions.db.ForeignKey(
            "picture.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_uid = extensions.db.Column(
        extensions.db.Integer,
        extensions.db.ForeignKey(
            "user.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_username = extensions.db.Column(
        extensions.db.String,
        nullable = False
    )


class Dislike(extensions.db.Model):
    id = extensions.db.Column(
        extensions.db.Integer,
        primary_key = True,
        nullable = False
    )

    uid = extensions.db.Column(
        extensions.db.Integer,
        unique = True,
        default = lambda: round(datetime.datetime.now(datetime.timezone.utc).timestamp())
    )
    date_created = extensions.db.Column(
        extensions.db.DateTime(timezone=True),
        default = datetime.datetime.now(datetime.timezone.utc)
    )
    picture_uid = extensions.db.Column(
        extensions.db.Integer,
        extensions.db.ForeignKey(
            "picture.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_uid = extensions.db.Column(
        extensions.db.Integer,
        extensions.db.ForeignKey(
            "user.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_username = extensions.db.Column(
        extensions.db.String,
        nullable = False
    )


class Comment(extensions.db.Model):
    id = extensions.db.Column(
        extensions.db.Integer,
        primary_key = True,
        nullable = False
    )

    uid = extensions.db.Column(
        extensions.db.Integer,
        unique = True,
        default = lambda: round(datetime.datetime.now(datetime.timezone.utc).timestamp())
    )
    date_created = extensions.db.Column(
        extensions.db.DateTime(timezone=True),
        default = datetime.datetime.now(datetime.timezone.utc)
    )
    text = extensions.db.Column(
        extensions.db.String,
        nullable = False
    )
    picture_uid = extensions.db.Column(
        extensions.db.Integer,
        extensions.db.ForeignKey(
            "picture.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_uid = extensions.db.Column(
        extensions.db.Integer,
        extensions.db.ForeignKey(
            "user.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_username = extensions.db.Column(
        extensions.db.String,
        nullable = False
    )
    status = extensions.db.Column(
        extensions.db.String,
        default = "normal"
    )


class View(extensions.db.Model):
    id = extensions.db.Column(
        extensions.db.Integer,
        primary_key = True,
        nullable = False
    )

    uid = extensions.db.Column(
        extensions.db.Integer,
        unique = True,
        default = lambda: round(datetime.datetime.now(datetime.timezone.utc).timestamp())
    )
    date_created = extensions.db.Column(
        extensions.db.DateTime(timezone=True),
        default = datetime.datetime.now(datetime.timezone.utc)
    )
    picture_uid = extensions.db.Column(
        extensions.db.Integer,
        extensions.db.ForeignKey(
            "picture.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_uid = extensions.db.Column(
        extensions.db.Integer,
        extensions.db.ForeignKey(
            "user.uid",
            ondelete = "CASCADE"
        ),
        nullable = False
    )
    author_username = extensions.db.Column(
        extensions.db.String,
        nullable = False
    )
