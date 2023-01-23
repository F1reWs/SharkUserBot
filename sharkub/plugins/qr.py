from pyrogram import Client, filters
from ..plugins.settings.main_settings import module_list, file_list
import qrcode

from ..prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("qr", prefixes=prefix) & filters.me)
async def qr(client, message):
    await message.edit('**Creating QRCode...**')

    img = qrcode.make(message.text[8:])
    img.save('assets/code.png')


    with open('assets/code.png', 'rb') as photo:
        await message.delete()
        await client.send_photo(message.chat.id, photo)


module_list["QRCode"] = {
    "qr [text]": "Create qrcode",
}
file_list["QRCode"] = "qr.py"