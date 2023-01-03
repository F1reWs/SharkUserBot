from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('support', prefixes=prefix) & filters.me)
async def support(client, message):
    await message.edit(f"**Support:** @MasterStroke777")

module_list['Support'] = f'{prefix}support'
file_list['Support'] = 'support.py'
