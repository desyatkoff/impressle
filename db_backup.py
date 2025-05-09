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
import time
import shutil
import datetime

import config


BACKUP_FILE_PATH = f"{config.DB_BACKUP_PATH}{datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')}-database.db~"


if __name__ == "__main__":
    """Create the database backup every day"""


    while True:
        if not os.path.exists(BACKUP_FILE_PATH):
            shutil.copy2(
                src = config.DB_PATH,
                dst = BACKUP_FILE_PATH
            )


        time.sleep(60 * 60 * 24)    # 24 hours

