from pyrogram import Client, filters
from time import sleep
from ..settings.main_settings import module_list, file_list

from ..settings.prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("redly", prefixes=prefix) & filters.me)
async def redly_spam(client, message):
  while True:  
    await message.edit(f"+rep")
    sleep(0.5)
    await message.edit(f"-rep")
    sleep(0.5)
    await message.edit(f"спс")
    sleep(0.5)


module_list["Example"] = {
"example_edit": "Description",
}
file_list["Example"] = "example.py"
