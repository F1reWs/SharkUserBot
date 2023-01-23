from pyrogram import Client, filters, __version__
from ..plugins.settings.main_settings import module_list, version, file_list
from telegraph import Telegraph
from platform import python_version
import psutil
from difflib import get_close_matches
from sharkub import utils

from ..prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('help', prefixes=prefix) & filters.me)
async def helps(client, message):
    await message.edit('<b>Loading the help menu. Please, wait...</b>')
    args = utils.get_args_raw(message)
    if args:
        match = get_close_matches(args, module_list.keys())
        if match:
            help_cmds = []
            modname = match[0]
            cmds = module_list[modname]
            for k, v in cmds.items():
                help_cmds.append(f"<code>{prefix}{k}</code> | <b>{v}</b>")
            
            text = """
<b>Help module </b><code>{}</code>

<b>Commands:</b>
{}
            """
            await message.edit(
                text.format(
                    modname,
                    "\n".join(help_cmds)
                )
            )
            return
        
    lists = []
    for k, v in module_list.items():
        lists.append(f'• {k}: {prefix}{f" | {prefix}".join(v.keys())}<br>')
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
<b>SharkUserBot v{version} RUNNING</b>

<b>Version: {version}</b>
<b>Modules: {len(module_list)}</b>
<b>Python: {python_version()}</b>
<b>Pyrogram: {__version__}</b>

<b><a href={link}>List of commands</a></b>
<b><a href="https://t.me/shark_userbot_support">💬 | SharkUserBot Support</a></b>
""", disable_web_page_preview=True)


@Client.on_message(filters.command('info', prefixes=prefix) & filters.me)
async def _info(client, message): 
    await message.edit("<b>Loading info... please wait</b>")
    lists = []
    for k, v in module_list.items():
        lists.append(f'• {k}: {v}<br>')
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
    cpu_p = psutil.cpu_percent()
    ram_u = int(dict(psutil.virtual_memory()._asdict())["used"])
    text = f"""
🦈 <b>SharkUserBot v{version}</b>

<b>Version: <i>{version}</i></b>
<b>Modules: <i>{len(module_list)}</i></b>
<b>Prefix: «{prefix}»</b>
<i>by @MasterStroke777</i>

<b>CPU usage:</b> <i>{cpu_p}%</i>
<b>RAM usage:</b> <i>{int(ram_u/1048576)} MB</i>

<b><a href="https://github.com/Master-Stroke/SharkUserBot">Github</a></b>
<b><a href={link}>List of commands</a></b>
<b><a href="https://t.me/shark_userbot_support">SharkUserBot Support</a></b>
"""
    try: 
      await client.send_animation(message.chat.id, "assets/banner.gif", caption=text, unsave=True)
      await message.delete()
    except:
      await message.edit(text=text, disable_web_page_preview=True)

@Client.on_message(filters.command('version', prefixes=prefix) & filters.me)
async def _version(client, message): 
   await message.edit(f"<b>SharkUserBot version: <i>{version}</i></b>")

module_list["Help"] = {
    "help": "Get all commands and other info",
    "info": "Info about userbot",
    "version": "Get userbot version"
}
file_list["Help"] = "help.py"
