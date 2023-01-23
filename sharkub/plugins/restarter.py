import os
import zipfile
import wget
import shutil
from pyrogram import Client, filters
from pyrogram.types import Message
from ..plugins.settings.main_settings import module_list, file_list

from ..prefix import my_prefix
prefix = my_prefix()


async def restart(message: Message, restart_type):
    if restart_type == "update":
        text = "1"
    else:
        text = "2"

    if os.name == "nt":
        await os.execvp(
            "python -m",
            [
                "python -m",
                "-m",
                "sharkub",
                f"{message.chat.id}",
                f"{message.message_id}",
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
                f"{message.message_id}",
                f"{text}",
            ],
        )


# Restart
@Client.on_message(filters.command("restart", prefixes=prefix) & filters.me)
async def restart_get(client, message):
  #  try:
        await message.edit("Restarting userbot...")
        await restart(message, restart_type="restart")
   # except:
  #      await message.edit("An error occured...")

module_list["Restarter"] = {
    "restart": "Restart userbot",
}
file_list["Restarter"] = "restart.py"