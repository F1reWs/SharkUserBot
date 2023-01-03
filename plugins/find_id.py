from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('id', prefixes=prefix) & filters.me)
async def find_id(client, message):
    if message.reply_to_message is None:
        await message.edit(f"Chat ID: `{message.chat.id}`")
    else:
        await message.edit(f"User ID: `{message.reply_to_message.from_user.id}`\nChat ID: `{message.chat.id}`")


module_list['FindIDThisChat'] = f'{prefix}id'
file_list['FindIDThisChat'] = 'find_id.py'
