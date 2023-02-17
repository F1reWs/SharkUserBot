#    SharkUB (telegram userbot by https://github.com/Master-Stroke)
#    Copyright (C) 2023 SharkUserBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    GNU General Public License https://www.gnu.org/licenses.

import logging
from importlib import import_module
import os

def logger():
    logging.basicConfig(
        filename="sharkub/temp/shark_userbot.log",
        filemode="w",
        format="%(asctime)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        level=logging.INFO
    )

def userbot():
    from pyrogram import Client
    from . import configurator
    from . import prestarter
    api_id, api_hash, device_mod = configurator.my_api()
    prestarter.prestart(api_id, api_hash, device_mod)
    Client = Client(
        "my_account",
        api_id=api_id,
        api_hash=api_hash,
        device_model=device_mod,
        plugins=dict(root="sharkub/modules")
    ).run()

if __name__ == "__main__":
    userbot()
    logger()