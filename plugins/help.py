from pyrogram import Client, filters, __version__
from plugins.settings.main_settings import module_list, version
from telegraph import Telegraph
from platform import python_version

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('help', prefixes=prefix) & filters.me)
async def helps(client, message):
    await message.edit('Loading the help menu. Please, wait...')
    lists = []
    for k, v in module_list.items():
        lists.append(f'➣ {k}: {v}<br>')
    a = " "
    for i in lists:
        a = a.lstrip() + f'{i}'
    helpes = f"""
{len(module_list)} available modules.<br>
<br>
{a}
"""
    telegraph = Telegraph()
    telegraph.create_account(short_name='SharkUserBot')
    link = f"https://telegra.ph/{telegraph.create_page('SharkUserbot Help', html_content=f'{helpes}')['path']}"
    await message.edit(f"""
<b>🦈 | SharkUserBot</b>
<b>📝 | Version: {version}</b>
<b>🐍 | Python: {python_version()}</b>
<b>⚙️ | Pyrogram: {__version__}</b>
<b>📁 | Modules: {len(module_list)}</b>

<b><a href={link}>❓ | List of commands</a></b>
<b><a href="https://github.com/Master-Stroke/SharkUserBot">🐈‍⬛ | Github</a></b>
""", disable_web_page_preview=True)


module_list['Help'] = f'{prefix}help'
