from pyrogram import Client, filters
from ..plugins.settings.main_settings import module_list, file_list

from ..prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("del", prefixes=prefix) & filters.me)
async def delete_messages(client, message):
    if message.reply_to_message:
        message_id = message.reply_to_message.id
        await client.delete_messages(message.chat.id, message_id)
    await message.delete()

module_list["DeleteMessage"] = {
    "del [reply]": "Delete Message",
}
file_list["DeleteMessage"] = "del.py"