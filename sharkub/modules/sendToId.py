from pyrogram import Client, filters
from ..settings.main_settings import module_list, file_list

from ..settings.prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("send", prefixes=prefix) & filters.me)
async def sendtoid(client, message):
    text = message.text.split(maxsplit=2)[2]
    await client.unblock_user(message.command[1])
    await client.send_message(message.command[1], text)
    await message.edit(f"Message sended to {message.command[1]}")


module_list["SendToUser"] = {
"send [ID | Username] [text]": "Send message to user",
}
file_list["sendToUser"] = "sendToId.py"