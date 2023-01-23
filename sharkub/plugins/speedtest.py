import asyncio
from pyrogram import Client, filters, types
from ..plugins.settings.main_settings import module_list, file_list
import speedtest

from ..prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("speedtest", prefix) & filters.me)
async def avatime(client, message):
  await message.edit("`Starting SpeedTest . . .`")
  spd = speedtest.Speedtest()
  result_dow = int(spd.download())
  await message.edit("`Starting SpeedTest . . . 50%`")
  result_upl = int(spd.upload())

  await message.edit(f"**Speedtest Results:**\n\n**Download:** `{round(result_dow/1000000, 2)}`** MiB/s**\n**Upload: **`{round(result_upl/1000000, 2)}` **MiB/s**")


module_list["Speedtest"] = {
"speedtest": "Check your internet with speedtest",
}
file_list["Speedtest"] = "speedtest.py"