#    SharkUB (telegram userbot by https://github.com/Master-Stroke)
#    Copyright (C) 2023 SharkUserBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    GNU General Public License https://www.gnu.org/licenses.

import os


def check_structure():
    if not os.path.exists("temp"):
        os.mkdir("temp")
    if not os.path.exists("temp/autoanswer_DB"):
        os.mkdir("temp/autoanswer_DB") 
