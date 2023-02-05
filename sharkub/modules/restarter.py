import os
import configparser
from pyrogram import Client, filters
from pyrogram.types import Message
from ..settings.main_settings import module_list, file_list

from ..settings.prefix import my_prefix
prefix = my_prefix()

config = configparser.ConfigParser()
config.read("config.ini")

lang = config.get("Language", "language")

if lang == "ru":
  string = {
      "restarting": "<i>Перезагрузка юзербота...</i>",
  }    

  module_list["Restarter"] = {
    "restart": "Restart userbot",
  }
  file_list["Restarter"] = "restart.py"

elif lang == "ua":
  string = {
      "restarting": "<i>Перезавантаження юзербота...</i>",
  }         

  module_list["Restarter"] = {
    "restart": "Restart userbot",
  }
  file_list["Restarter"] = "restart.py"

else:
  string = {
      "restarting": "<i>Restarting userbot...</i>",
  }       

  module_list["Restarter"] = {
    "restart": "Restart userbot",
  }
  file_list["Restarter"] = "restart.py"

async def restart(message, restart_type):
    if restart_type == "update":
        text = "1"
    else:
        text = "2"

    try:
        msg_id = message.message_id
    except:
        msg_id = message.id        

    if os.name == "nt":
        await os.execvp(
            "python -m",
            [
                "python -m",
                "-m",
                "sharkub",
                f"{message.chat.id}",
                f"{msg_id}",
                f"{text}",
            ],
        )
    else:
        await os.execvp(
            "python3",
            [
                "python3",
                "-m",
                "sharkub",
                f"{message.chat.id}",
                f"{msg_id}",
                f"{text}",
            ],
        )



# Restart
@Client.on_message(filters.command("restart", prefixes=prefix) & filters.me)
async def restart_get(client, message):
        await message.edit(string['restarting'])
        await restart(message, restart_type="restart")