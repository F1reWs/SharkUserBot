import wget
from pyrogram import Client, filters
from plugins.restarter import restart
from plugins.settings.main_settings import module_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('loadmod', prefixes=prefix) & filters.me)
async def loadmod(client, message):
    if not message.reply_to_message:
        await message.edit("<b>Load module...</b>")
        link = message.command[1]
        wget.download(link, 'plugins/')
        await message.edit(
            f"<b>**The module has been loaded successfully.**\nRestart..."
        )
        await restart(message, restart_type="restart")
    else:
        await client.download_media(message.reply_to_message.document, file_name='plugins/')
        await message.edit(
            f"<b>**The module has been loaded successfully.**\nRestart..."
        )
        await restart(message, restart_type="restart")


module_list['Loadmod'] = f'{prefix}loadmod [link to the module]'
