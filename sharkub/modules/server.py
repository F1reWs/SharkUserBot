import asyncio
from pyrogram import Client, filters, types
import psutil
import time
from ..settings.main_settings import module_list, file_list

from ..settings.prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("server", prefix) & filters.me)
async def avatime(client, message):
    cpu_f = dict(psutil.cpu_freq()._asdict())["current"]
    cpu_p = psutil.cpu_percent()
    disk_t = dict(psutil.disk_usage('/')._asdict())["total"]
    disk_u = dict(psutil.disk_usage('/')._asdict())["used"]
    disk_p = dict(psutil.disk_usage('/')._asdict())["percent"]
    ram_t = int(dict(psutil.virtual_memory()._asdict())["total"])
    ram_u = int(dict(psutil.virtual_memory()._asdict())["used"])
    ram_p = int(dict(psutil.virtual_memory()._asdict())["percent"])
    swap_t = int(dict(psutil.swap_memory()._asdict())["total"])
    swap_u = int(dict(psutil.swap_memory()._asdict())["used"])
    swap_p = int(dict(psutil.swap_memory()._asdict())["percent"])

    text = f"""**<emoji id=4988254788001989201>⚙️</emoji> Server Info:**
**CPU loaded** `{cpu_p}%`
**CPU frequency **`{cpu_f}` **MHz**
**RAM busy:** `{int(ram_u/1048576)}` **from** `{int(ram_t/1048576)}` **MB -**`{ram_p}%`
**Swap busy: **`{int(swap_u/1048576)}` **from** `{int(swap_t/1048576)}`** MB -**`{swap_p}%`
**Disk busy: **`{int(disk_u/1048576)}` **from** `{int(disk_t/1048576)}`** MB -** `{disk_p}%`
"""
    await message.edit(text)

module_list["Server"] = {
"server": "Information abour server",
}
file_list["Server"] = "server.py"
