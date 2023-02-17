#    SharkUB (telegram userbot by https://github.com/Master-Stroke)
#    Copyright (C) 2023 SharkUserBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    GNU General Public License https://www.gnu.org/licenses.

import os
import sys
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


def get_prefix():
    prefix = config.get("prefix", "prefix")
    return prefix


def my_prefix():
    try:
        prefix = get_prefix()
    except:
        config.add_section("prefix")
        config.set("prefix", "prefix", ".")
        with open("./config.ini", "w") as config_file:
            config.write(config_file)
        prefix = "."
    return prefix
