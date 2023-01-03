from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
from time import sleep
import datetime

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("tn", prefixes=prefix) & filters.me)
def time_name(client, msg):
   msg.edit(f"**Успешно поставил время в профиле!**")
   while True:
      Hour = int(datetime.datetime.now().strftime("%H"))
      Minute = datetime.datetime.now().strftime("%M")
      client.update_profile(last_name=f"| {Hour}:{Minute} ᵗⁱᵐᵉ")
      sleep(30)  


module_list['TimeName'] = f'{prefix}tn'
file_list['TimeName'] = 'time_name.py'
