#    SharkUB (telegram userbot by https://github.com/Master-Stroke)
#    Copyright (C) 2023 SharkUserBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    GNU General Public License https://www.gnu.org/licenses.

import configparser
from pyrogram import Client, filters
from time import perf_counter
from ..settings.main_settings import module_list, file_list

from ..settings.prefix import my_prefix
prefix = my_prefix()

config = configparser.ConfigParser()
config.read("config.ini")

lang = config.get("Language", "language")

if lang == "ru":
  string = {
      "stable": f"<emoji id=5017221456195486453>🟢</emoji> Стабильный",
      "good": f"<emoji id=5017036832731300473>🟠</emoji> Хорошый",
      "unstable": f"<emoji id=5062246560432128687>🔴</emoji> Не стабильный",
      "bad": f"⚠ Проверьте свое подключение к интернету",
      "pong": f"<b>🏓 Понг\n<emoji id=5220226955206467824>📶</emoji></b>",
  }   

  module_list["Ping"] = {
    "ping": "Свой пинг",
  }
  file_list["Ping"] = "ping.py"

elif lang == "ua":
  string = {
      "stable": f"<emoji id=5017221456195486453>🟢</emoji> Стабільний",
      "good": f"<emoji id=5017036832731300473>🟠</emoji> Добре",
      "unstable": f"<emoji id=5062246560432128687>🔴</emoji> Нестабільний",
      "bad": f"⚠ Check you network connection",
      "pong": f"<b>🏓 Понг\n<emoji id=5220226955206467824>📶</emoji></b>",
  }   

  module_list["Ping"] = {
    "ping": "Свій пінг",
  }
  file_list["Ping"] = "ping.py" 

else:
  string = {
      "stable": f"<emoji id=5017221456195486453>🟢</emoji> Stable",
      "good": f"<emoji id=5017036832731300473>🟠</emoji> Good",
      "unstable": f"<emoji id=5062246560432128687>🔴</emoji> Unstable",
      "bad": f"⚠ Check you network connection",
      "pong": f"<b>🏓 Pong\n<emoji id=5220226955206467824>📶</emoji></b>",
  }    

  module_list["Ping"] = {
    "ping": "Show your ping",
  }
  file_list["Ping"] = "ping.py"

@Client.on_message(filters.command('ping', prefixes=prefix) & filters.me)
async def ping(client, message):
    start = perf_counter()
    await message.edit("🏓 ⚾=== 🏓")
    await message.edit("🏓 =⚾== 🏓")
    await message.edit("🏓 ==⚾= 🏓")
    await message.edit("🏓 ===⚾ 🏓")
    end = perf_counter()

    pinges = ((end - start) / 4)
    ping = pinges * 1000

    if 0 <= ping <= 199:
        connect = string['stable']
    if 199 <= ping <= 400:
        connect = string['good']
    if 400 <= ping <= 600:
        connect = string['unstable']
    if 600 <= ping:
        connect = string['bad']
    await message.edit(f"{string['pong']} {round(ping)} ms\n{connect}")