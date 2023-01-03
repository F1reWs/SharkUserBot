from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
from datetime import datetime

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("time", prefixes=prefix) & filters.me)
async def time(client, message):
    now = datetime.datetime.now().strftime("Date: %d/%m/%Y\nTime: %H:%M:%S")
    await message.edit(now)


module_list['TimeNow'] = f'{prefix}time'
file_list['TimeNow'] = 'time_now.py'
