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
