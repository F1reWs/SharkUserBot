from pyrogram import Client, filters
from ..settings.main_settings import module_list, file_list
from ..modules.restarter import restart
import configparser
import os
import sys

from ..settings.prefix import my_prefix
prefix = my_prefix()


config = configparser.ConfigParser()
config.read("config.ini")

lang = config.get("Language", "language")

if lang == "ru":
  string = {  
    "prefix_none": "<b>Префикс не может быть пустим!</b>",
    "prefix_setted1": f"<emoji id=5197474765387864959>✅</emoji> <b>Префикс",
    "prefix_setted2": f"поставлен!</b>\nПерезагрузка юзербота...",
    "defined": f"<b>Используйте <code>{prefix}setlang</code> [en/ru/ua]!</b>",
  }

  module_list["Setttings"] = {
    "sp [новый_префикс]": "Поставить новый префикс юзерботу",
    "setlang [en/ru/ua]": "Выбрать язык юзерботу",
  }

  file_list["Setprefix"] = "settings.py"

elif lang == "ua":
  string = {  
    "prefix_none": "<b>Префікс не може бути порожнім!</b>",
    "prefix_setted1": f"<emoji id=5197474765387864959>✅</emoji> <b>Префікс",
    "prefix_setted2": f"поставлено!</b>\nПерезавантаження юзербота...",
    "defined": f"<b>Используйте <code>{prefix}setlang</code> [en/ru/ua]!</b>",    
  }

  module_list["Setttings"] = {
    "sp [новий_префікс]": "Поставити новий префікс юзерботу",
    "setlang [[en/ru/ua]": "Вибрати мову юзерботу",
  }

  file_list["Setprefix"] = "settings.py"  

else:
  string = {
      "prefix_none": "<b>Prefix can't be emty!</b>",
      "prefix_setted1": f"<emoji id=5197474765387864959>✅</emoji> <b>Prefix",
      "prefix_setted2": f"set!</b>\nRestarting userbot...",
      "defined": f"<b>Use <code>{prefix}setlang [en/ru/ua]</code>!</b>",
  }    

  module_list["Settings"] = {
    "sp [new_prefix]": "Set new prefix to userbot",
    "setlang [en/ru/ua]": "Choose language to userbot",
  }

  file_list["Settings"] = "settings.py"

@Client.on_message(filters.command(["sp", "setprefix"], prefixes=prefix) & filters.me)
async def sprefix(client, message):
    if len(message.command) > 1:
        prefixgett = message.command[1]
        config.set("prefix", "prefix", prefixgett)
        with open("config.ini", "w") as config_file:
            config.write(config_file)    
        await message.edit(
            text = f"{string['prefix_setted1']} [ <code>{prefixgett}</code> ] {string['prefix_setted2']}"
        )
        await restart(message, restart_type="restart")
    else:
        await message.edit(text = (f"{string['prefix_none']}"))

@Client.on_message(filters.command(["sl", "setlang"], prefixes=prefix) & filters.me)
async def setlang(client, message):
    if len(message.command) > 1:
        langget = message.command[1]
        if langget == "ru" or langget == "russian":
           langset = "ru"
           say = f"<b><emoji id=6323139226418284334>🇷🇺</emoji> Язык сохранён!</b>\n<i>Перезагрузка юзербота...</i>"
        elif langget == "en" or langget == "english":
           langset = "en"
           say = f"<b><emoji id=6323589145717376403>🇬🇧</emoji> Language saved!</b>\n<i>Restarting userbot...</i>"
        elif langget == "ua" or langget == "ukrainian":
           langset = "ua"
           say = f"<b><emoji id=6323289850921354919>🇺🇦</emoji> Мова збережена!</b>\n<i>Перезавантаження юзербота...</i>"
        else:
           await message.edit(
            string["defined"]
            )
           return              
        config.set("Language", "language", langset)
        with open("config.ini", "w") as config_file:
            config.write(config_file)
        await message.edit(
            say
        )
        await restart(message, restart_type="restart")
    else:
        await message.edit(string["defined"])