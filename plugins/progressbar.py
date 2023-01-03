from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import time

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("progressbar", prefixes=prefix) & filters.me)
async def progressbar(client, message):
    text = message.text.split(prefix + "progressbar ", maxsplit=1)[1]

    total = 100
    bar_length = 10
    for i in range(total + 1):
        percent = 100.0 * i / total
        time.sleep(0.1)
        await message.edit(
            text + "\n[{:{}}] {:>3}%".format("█" * int(percent / (100.0 / bar_length)), bar_length, int(percent)))

module_list['Progressbar'] = f'{prefix}progressbar [Text]'
file_list['Progressbar'] = 'progressbar.py'
