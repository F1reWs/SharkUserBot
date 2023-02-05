import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
from ..settings.main_settings import module_list, file_list

from ..settings.prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("spam", prefixes=prefix) & filters.me)
def spam(client, msg):
    msg.delete()
    text = msg.text.split(maxsplit=2)[2]
    n = msg.text.split(maxsplit=2)[1]

    for _ in range(int(n)):
        try:
            client.send_message(msg.chat.id, text)
        except FloodWait as e:
            sleep(e.x)


module_list["Spam"] = {
"spam [amount] [text]": "Spam text in chat",
}
file_list["Spam"] = "spam.py"