import asyncio
import datetime
from pyrogram import Client, filters, types
from ..plugins.settings.main_settings import module_list, file_list
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta

from ..prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("avatime", prefix) & filters.me)
async def avatime(client, message):
  await message.edit_text("<b>Creating picture...</b>")
  while True:
    Second = datetime.now().strftime("%S")
    if Second == "00":
      await message.edit_text("Done!")
      break
  while True:
    Hour = datetime.now().strftime("%H")
    Minute = datetime.now().strftime("%M")
    image = Image.new("RGB", (1000, 1000), "black")
    font = ImageFont.truetype("assets/Machine BT.ttf", 250)
    draw = ImageDraw.Draw(image)
    draw.text((500, 500), f"{Hour}:{Minute}", anchor = "mm", fill = "green", font = font)
    image.save("assets/avatime.png")
    await client.set_profile_photo(photo="assets/avatime.png")
    await asyncio.sleep(60)
    photos = [p async for p in client.get_chat_photos("me")]
    await client.delete_profile_photos([p.file_id for p in photos[1:]])

module_list["Avatime"] = {
    "avatime": "Make on your ava time",
}
file_list["Avatime"] = "avatime.py"