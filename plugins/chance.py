from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import random

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("chance", prefixes=prefix) & filters.me)
async def chance(client, message):
    text = message.text.split(prefix + "chance ", maxsplit=1)[1]
    await message.edit(f"{text}\nChance: {random.randint(1, 100)}%")


module_list['Chance'] = f'{prefix}chance [Text]'
file_list['Chance'] = 'chance.py'
