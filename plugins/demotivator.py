import asyncio
from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()

username_dem = "KlounsBot"

@Client.on_message(filters.command("dem", prefixes=prefix) & filters.me)
async def demotivator(client, message):
    await message.edit("Creating demotivator..")
    if message.reply_to_message.photo:
        await client.unblock_user(username_dem)
        capt = message.text.split(prefix + "dem ", maxsplit=1)[1]
        await client.send_photo(
            chat_id=username_dem,
            photo=message.reply_to_message.photo.file_id,
            caption=capt
        )
        photo = False

        while not photo:
            try:
                await asyncio.sleep(2)
                async for iii in client.get_chat_history(username_dem, limit=1):
                    await client.send_photo(chat_id=message.chat.id, photo=iii.photo.file_id)
                photo = True
                await message.delete()
            except Exception as f:
                await message.edit(f)
                await asyncio.sleep(2)
    else:
        await message.edit("Please, reply to photo")


module_list['Demotivator'] = f'{prefix}dem [reply to photo]'
file_list['Demotivator'] = 'demotivator.py'
