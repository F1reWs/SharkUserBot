from pyrogram import Client, filters
from telegraph import upload_file
import os
from ..settings.main_settings import module_list, file_list

from ..settings.prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command(["tm", "tgm", "telegraph"], prefix) & filters.me)
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.edit("reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4")
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.edit("not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message, file_name="downloads"
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.edit(message.chat.id, document)
    else:
        await message.edit(
            f"**Document passed to: [Telegra.ph](https://telegra.ph{response[0]})**",
        )
    finally:
        os.remove(download_location)    


module_list["Telegraph"] = {
"tm [reply_media]": "Put image on telegraph",
}
file_list["Telegraph"] = "telegraph.py"