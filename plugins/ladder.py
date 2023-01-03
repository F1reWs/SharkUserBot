from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("ladder", prefixes=prefix) & filters.me)
async def ladder(client, message):
    orig_text = message.text.split(prefix + "ladder ", maxsplit=1)[1]
    text = orig_text
    output = []
    for i in range(len(text) + 1):
        output.append(text[:i])
    ot = "\n".join(output)
    await message.edit(ot)


module_list['Ladder'] = f'{prefix}ladder [text]'
file_list['Ladder'] = 'ladder.py'
