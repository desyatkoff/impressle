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


import os

import config
import website


app = website.init_flask_app()


if __name__ == "__main__":
    if not os.path.exists(config.DB_PATH):
        with app.app_context():
            website.extensions.db.create_all()


    app.run(
        host = config.HOST,
        port = config.PORT,
        debug = config.DEBUG_MODE
    )
