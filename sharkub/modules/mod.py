import wget
import configparser
from pyrogram import Client, filters
from ..modules.restarter import restart
from ..settings.main_settings import module_list

from ..settings.prefix import my_prefix
prefix = my_prefix()

config = configparser.ConfigParser()
config.read("config.ini")

lang = config.get("Language", "language")

if lang == "ru":
  string = {
      "load_mod": "<b>Загрузка модуля...</b>",
      "loaded": "<b>Модуль был успешно загружен</b>\n<i>Перезагрузка...</i>",
  }    

  module_list["Loadmodule"] = {
    "loadmod [ссылка на модуль]": "Загрузить модуль из ссылки в файл",
    "loadmod [ответ]": "Загрузить модуль из файла ответа",
  }

elif lang == "ua":
  string = {
      "load_mod": "<b>Завантаження модуля...</b>",
      "loaded": "<b>Модуль успішно завантажен.</b>\n<i>Перезавантаження...</i>",
  }      

  module_list["Loadmodule"] = {
    "loadmod [посилання_на_файл]": "Завантажити модуль із посилання на фай",
    "loadmod [відповідь]": "Завантажити модуль із файлу відповіді",
  }

else:
  string = {
      "load_mod": "<b>Loading module...</b>",
      "loaded": "<b>The module has been loaded successfully.</b>\n<i>Restarting...</i>",
  }    

  module_list["Loadmodule"] = {
    "loadmod [link to the module]": "Load module from link to file",
    "loadmod [reply]": "Load module from reply file",
  }

@Client.on_message(filters.command('loadmod', prefixes=prefix) & filters.me)
async def loadmod(client, message):
    if not message.reply_to_message:
        await message.edit(string[load_mod])
        link = message.command[1]
        wget.download(link, 'sharkub/modules/')
        await message.edit(
            string[loaded]
        )
        await restart(message, restart_type="restart")
    else:
        await client.download_media(message.reply_to_message.document, file_name='custom/modules/')
        await message.edit(
            string[loaded]
        )
        await restart(message, restart_type="restart")