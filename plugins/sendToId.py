from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("send", prefixes=prefix) & filters.me)
async def sendtoid(client, message):
    await client.unblock_user(message.command[1])
    await client.send_message(message.command[1], "Hi")
    await message.edit(f"Message send to {message.command[1]}")


module_list['SendToId'] = f'{prefix}send [ID | Username]'
file_list['SendToId'] = 'SendToId.py'
