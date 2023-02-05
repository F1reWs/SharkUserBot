from pyrogram import Client, filters
from ..settings.main_settings import module_list, file_list

from ..settings.prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("example_edit", prefixes=prefix) & filters.me)
async def example_edit(client, message):
    await message.edit("<code>This is an example module</code>")

module_list["Example"] = {
"example_edit": "Description",
}
file_list["Example"] = "example.py"
