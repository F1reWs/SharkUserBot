#    SharkUB (telegram userbot by https://github.com/Master-Stroke)
#    Copyright (C) 2023 SharkUserBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    GNU General Public License https://www.gnu.org/licenses.

import wget
import os
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
      "systemmod": "<b>Невозможно удалить системный модуль, это нарушить работу юзербота!</b>",
      "error_install": "<b>Ошибка с установкой модуля</b>",
      "modd": "Модуль",
      "notfound": "не найден",
      "unloaded": "выгружено",
      "unloading": "<i>Выгрузка модуля...</i>",
      "use": "Используй",
      "modname": "название модуля",
  }    

  module_list["Loadmodule"] = {
    "dlmod [ссылка на модуль]": "Загрузить модуль из ссылки в файл",
    "dlmod [ответ]": "Загрузить модуль из файла ответа",
    "unloadmod [модуль]": "Выгрузить модуль с юзербота",
  }

elif lang == "ua":
  string = {
      "load_mod": "<b>Завантаження модуля...</b>",
      "loaded": "<b>Модуль успішно завантажен.</b>\n<i>Перезавантаження...</i>",
      "systemmod": "<b>Неможливо видалити системний модуль, це порушить роботу юзербота!</b>",
      "error_install": "<b>Помилка під час встановлення модуля</b>",
      "modd": "Модуль",
      "notfound": "не знайшло",
      "unloaded": "вивантажено",
      "unloading": "<i>Вивантаження модуля...</i>",
      "use": "Використовуй",
      "modname": "назва модуля",
  }      

  module_list["Loadmodule"] = {
    "dlmod [посилання_на_файл]": "Завантажити модуль із посилання на фай",
    "dlmod [відповідь]": "Завантажити модуль із файлу відповіді",
    "unloadmod [модуль]": "Вивантажити модуль із юзербота",
  }

else:
  string = {
      "load_mod": "<b>Loading module...</b>",
      "loaded": "<b>The module has been loaded successfully.</b>\n<i>Restarting...</i>",
      "systemmod": "<b>Cannot remove system module, it will disrupt userbot!</b>",
      "error_install": "<b>Error with installing module</b>",
      "modd": "Module",
      "notfound": "не знайдено",
      "unloaded": "unloaded",
      "unloading": "<i>Unloading module...</i>",
      "use": "Use",
      "modname": "module name",
  }    

  module_list["Loadmodule"] = {
    "dlmod [link to the module]": "Load module from link to file",
    "dlmod [reply]": "Load module from reply file",
    "unloadmod [module]": "Unload module from userbot",
  }

@Client.on_message(filters.command(['loadmod', 'dlmod'], prefixes=prefix) & filters.me)
async def loadmod(client, message):
    if not message.reply_to_message:
        await message.edit(string['load_mod'])
        try:
          link = message.command[1]
          wget.download(link, 'sharkub/modules/custom_modules')
        except:
          await message.edit(string['error_install'])
          return
        await message.edit(
            string['loaded']
        )
        await restart(message, restart_type="restart")
    else:
        await message.edit(
          string['load_mod']
        )
        try:
          await client.download_media(message.reply_to_message.document, file_name='modules/custom_modules/')
        except:
          await message.edit(string['error_install'])
          return
        await message.edit(
            string['loaded']
        )
        await restart(message, restart_type="restart")

@Client.on_message(filters.command(['unloadmod'], prefixes=prefix) & filters.me)
async def unloadmod(client, message):
  await message.edit(string['unloading'])
  try:
    mod = message.command[1]
  except:
    await message.edit(f"<b>{string['use']}:</b>\n<code>{prefix}unloadmod</code> <b>[{string['modname']}]</b>")

  if os.path.exists(f"sharkub/modules/custom_modules/{mod}.py"):
        os.remove(f"sharkub/modules/custom_modules/{mod}.py")
        await message.edit(f"<b>{string['modd']} <code>{mod}</code> {string['unloaded']}!</b>")
  elif os.path.exists(f"sharkub/modules/{mod}.py"):
        await message.edit(
            string['systemmod']
        )
  else:
        await message.edit(f"<b>{string['modd']} <code>{mod}</code> {string['notfound']}</b>")