from pyrogram import Client, filters
from ..plugins.settings.main_settings import module_list, file_list, version

from ..prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('support', prefixes=prefix) & filters.me)
async def _support(client, message):
    await message.edit(f"<b>Loading information... Please wait</b>")
    text = f"""
<b>SharkUserBot Support</b>

<a href=https://github.com/Master-Stroke/SharkUserBot><b>Github</b></a>
<b>Version:</b> <i>{version}</i>
<b>News: @shark_userbot</b>
<b>Support chat: @shark_userbot_support</b>
<b>Main developer: @MasterStroke777</b>
<b>Modules: {len(module_list)}</b>
"""
    try:
      await client.send_animation(message.chat.id, "assets/support.gif", caption=text, unsave=True)
      await message.delete()
    except:
      await message.edit(text=text, disable_web_page_preview=True)

module_list['Support'] = f'{prefix}support'
file_list['Support'] = 'support.py'

module_list["Support"] = {
"support": "Show support links",
}
file_list["Support"] = "support.py"