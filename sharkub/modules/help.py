from pyrogram import Client, filters, __version__
from ..settings.main_settings import module_list, version, file_list
from telegraph import Telegraph
from platform import python_version
import psutil
import configparser
from difflib import get_close_matches
from sharkub import utils

from ..settings.prefix import my_prefix
prefix = my_prefix()

config = configparser.ConfigParser()
config.read("config.ini")

lang = config.get("Language", "language")

if lang == "ru":
  string = {
      "help_module": """<b>Помощь по модулю </b><code>{}</code>

<b>Команды:</b>
{}""",
      "loading_menu": f"<b>Загрузка меню. Пожалуйста, подождите...b>",
      "available": f"доступно модулей.",
      "version": f"версия",
      "loading_info": f"<b>Загрузка меню... Пожалуйста, подождите</b>",
  }    

  module_list["Help"] = {
    "help": "Получить все команды",
    "info": "Информация о юзерботе",
    "version": "Получить версию юзербота",
    "support": "Показать ссылки помощи",
  }
  file_list["Help"] = "help.py"

elif lang == "ua":
  string = {
      "help_module": """<b>Допомога по модулю </b><code>{}</code>

<b>Команди:</b>
{}""",
      "loading_menu": f"<b>Завантаження меню. Будь ласка, зачекайте...</b>",
      "available": f"доступно модулів.",
      "version": f"версія",
      "loading_info": f"<b>Завантаження інформації... Будь ласка, зачекайте...</b>",
  }    

  module_list["Help"] = {
    "help": "Отримати всі команди",
    "info": "Інформація про юзербота",
    "version": "Отримати версію юзербота",
    "support": "Показати посилання підтримки",
  }
  file_list["Help"] = "help.py"

else:
  string = {
      "help_module": """<b>Help module </b><code>{}</code>

<b>Commands:</b>
{}""",
      "loading_menu": "<b>Loading the help menu. Please, wait...</b>",
      "available": f"available modules.",
      "version": f"version",
      "loading_info": f"<b>Loading information... Please, wait</b>",
  }    

  module_list["Help"] = {
    "help": "Get all commands",
    "info": "Info about userbot",
    "version": "Get userbot version",
    "support": "Show support links",
  }
  file_list["Help"] = "help.py"


@Client.on_message(filters.command('help', prefixes=prefix) & filters.me)
async def helps(client, message):
    await message.edit(string['loading_menu'])
    args = utils.get_args_raw(message)
    if args:
        match = get_close_matches(args, module_list.keys())
        if match:
            help_cmds = []
            modname = match[0]
            cmds = module_list[modname]
            for k, v in cmds.items():
                help_cmds.append(f"<code>{prefix}{k}</code> | <b>{v}</b>")
            
            text = string["help_module"]
            await message.edit(
                text.format(
                    modname,
                    "\n".join(help_cmds)
                )
            )
            return
        
    lists = []
    for k, v in module_list.items():
        lists.append(f'• <b>{k}:</b> (<i>{prefix}{f" | {prefix}".join(v.keys())}</i>)\n')
    a = " "
    for i in lists:
        a = a.lstrip() + f'{i}'
    helpes = f"""
<b><emoji id=5334882760735598374>📝</emoji> {len(module_list)} {string['available']}</b><br>
<br>
{a}
"""
    await message.edit(helpes, disable_web_page_preview=True)


@Client.on_message(filters.command('info', prefixes=prefix) & filters.me)
async def _info(client, message): 
    await message.edit(string['loading_info'])
    cpu_p = psutil.cpu_percent()
    ram_u = int(dict(psutil.virtual_memory()._asdict())["used"])
    text = f"""
<emoji id=5787544344906959608>🦈</emoji> <b>SharkUserBot v{version}</b>

<b>Version: <i>{version}</i></b>
<b>Modules: <i>{len(module_list)}</i></b>
<b>Prefix: «{prefix}»</b>
<i>by @MasterStroke777</i>

<b>CPU usage:</b> <i>{cpu_p}%</i>
<b>RAM usage:</b> <i>{int(ram_u/1048576)} MB</i>

<b><a href="https://github.com/Master-Stroke/SharkUserBot">Github</a></b>
<b><a href="https://t.me/shark_userbot">SharkUserBot News</a></b>
<b><a href="https://t.me/shark_userbot_support">SharkUserBot Support</a></b>
"""
    try: 
      await client.send_animation(message.chat.id, "assets/banner.gif", caption=text, unsave=True)
      await message.delete()
    except:
      await message.edit(text=text, disable_web_page_preview=True)

@Client.on_message(filters.command('version', prefixes=prefix) & filters.me)
async def _version(client, message): 
   await message.edit(f"<b><emoji id=5334882760735598374>📝</emoji> SharkUserBot {string['version']}: <i>{version}</i></b>")

@Client.on_message(filters.command('support', prefixes=prefix) & filters.me)
async def _support(client, message):
    await message.edit(string['loading_info'])
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