#    SharkUB (telegram userbot by https://github.com/Master-Stroke)
#    Copyright (C) 2023 SharkUserBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    GNU General Public License https://www.gnu.org/licenses.

from typing import Union
from pyrogram import types
from sharkub.settings.prefix import my_prefix as prefix
from typing import Union


def get_args_raw(message: types.Message) -> Union[str, None]:
    text = message.text or message.caption
    if len(text.split(" ")) == 1: # if no arguments
        return None
    
    return " ".join(text.split(" ")[1:])