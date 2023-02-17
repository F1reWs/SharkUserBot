#    SharkUB (telegram userbot by https://github.com/Master-Stroke)
#    Copyright (C) 2023 SharkUserBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    GNU General Public License https://www.gnu.org/licenses.

import sys
import configparser
from pyrogram import Client, filters
from io import StringIO
from ..settings.main_settings import module_list, file_list

from ..settings.prefix import my_prefix
prefix = my_prefix()

config = configparser.ConfigParser()
config.read("config.ini")

lang = config.get("Language", "language")

if lang == "ru":
  string = {
      "code": f"<b><emoji id=4985626654563894116>💻</emoji> Код:</b>\n",
      "success": f"<b><emoji id=5197688912457245639>✅</emoji> Результат</b>:\n",
      "error": f"<b><emoji id=5852812849780362931>❌</emoji> Ошибка</b>:\ns",
  }    

  module_list["PythonShell"] = {
    "py [command]": "Write commands in PythonShell",
  }
  file_list["PythonShell"] = "eval.py"

elif lang == "ua":
  string = {
      "code": f"<b><emoji id=4985626654563894116>💻</emoji> Код:</b>\n",
      "success": f"<b><emoji id=5197688912457245639>✅</emoji> Результат</b>:\n",
      "error": f"<b><emoji id=5852812849780362931>❌</emoji> Помилка</b>:\ns",
  }    

  module_list["PythonShell"] = {
    "py [команда]": "Пишите команды в PythonShell.",
  }
  file_list["PythonShell"] = "eval.py" 

else:
  string = {
      "code": f"<b><emoji id=4985626654563894116>💻</emoji> Code:</b>\n",
      "success": f"<b><emoji id=5197688912457245639>✅</emoji> Result</b>:\n",
      "error": f"<b><emoji id=5852812849780362931>❌</emoji> Error</b>:\ns",
  }    

  module_list["PythonShell"] = {
    "py [command]": "Write commands in PythonShell",
  }
  file_list["PythonShell"] = "eval.py"

@Client.on_message(filters.command(["py", "eval", "e"], prefixes=prefix) & filters.me)
def user_exec(client, message):
    r = message.reply_to_message
    code = ""
    try:
        code = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        try:
            code = message.text.split(" \n", maxsplit=1)[1]
        except IndexError:
            pass

    result = sys.stdout = StringIO()
    try:
        exec(code)

        message.edit(
            f"{string['code']}"
            f"<code>{code}</code>\n\n"
            f"{string['success']}"
            f"<code>{result.getvalue()}</code>"
        )
    except:
        message.edit(
            f"{string['code']}"
            f"<code>{code}</code>\n\n"
            f"{string['error']}"
            f"<code>{sys.exc_info()[0].__name__}: {sys.exc_info()[1]}</code>"
        )