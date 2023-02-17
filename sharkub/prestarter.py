#    SharkUB (telegram userbot by https://github.com/Master-Stroke)
#    Copyright (C) 2023 SharkUserBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    GNU General Public License https://www.gnu.org/licenses.

from pyrogram import Client, filters
from sharkub.settings.prefix import my_prefix
import sys
import os
import time
import pip
import configparser
import datetime

prefix = my_prefix()

def prestart(api_id, api_hash, device_mod):
    app = Client("my_account", api_id=api_id, api_hash=api_hash, device_model=device_mod)

    config = configparser.ConfigParser()
    config.read("config.ini")

    lang = config.get("Language", "language")

    if lang == "ru":
     string = {
      "restarted": "<b>Юзербот успешно перезагружен</b>",
    }    

    elif lang == "ua":
     string = {
      "restarted": "<b>Юзербот успішно перезавантажений</b>",
    }         

    else:
      string = {
      "restarted": "<b>Userbot succesfully Restarted</b>",
    } 
    with app:
        if len(sys.argv) == 4:
            restart_type = sys.argv[3]
            requirements = [
                "install",    
                "pyrogram",
                "utils",
                "wheel",
                "telegraph",
                "requests",
                "wget",
                "rich",
                "wikipedia",
                "gTTS",
                "datetime",
                "qrcode",
                "speedtest-cli",
                "psutil",
                "tgcrypto",
                "aiohttp",
                "pillow",
                "termcolor",
                "openai"
                ]
            pip.main(requirements)
            text = string['restarted']
            try: 
              app.send_message("me", text)
            except Exception as f:
                app.send_message("me", f"Got error: {f}\n\n" + text)
                pass
        else:
          now = datetime.datetime.now()
          app.send_message("me", f"""
<b>[{now}] SharkUserBot Started!</b> 

<b>News: @Shark_UserBot</b>
<b>Custom modules: @SharkUBmodules_bot</b>
<b>Support: @Shark_UserBot_support</b>
<b>Offtop: @Sharkub_Offtop</b>

<b>For restart, enter:</b>
<code>{prefix}restart</code>
          """)

        app.join_chat("shark_userbot")
        time.sleep(1)
        app.join_chat("shark_userbot_support")
