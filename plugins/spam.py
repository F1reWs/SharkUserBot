import asyncio
from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("stspam", prefixes=prefix) & filters.me)
async def sticker_spam(client, message):
    if not message.text.split(prefix + "stspam", maxsplit=1)[1]:
        await message.edit("<i>Error</i>")

    sticker = message.command[3]
    count = int(message.command[1])
    sleep = int(message.command[2])
    await message.delete()

    for _ in range(count):
        await client.send_sticker(message.chat.id, sticker)
        await asyncio.sleep(sleep)


@Client.on_message(filters.command("spam", prefixes=prefix) & filters.me)
async def spam(client, message):
    if not message.text.split(prefix + "spam", maxsplit=1)[1]:
        await message.edit("<i>Error</i>")
        return
    count = message.command[1]
    text = " ".join(message.command[3:])
    count = int(count)
    try:
        sleep = int(message.command[2])
    except Exception as error:
        await message.edit(error)
        sleep = float(message.command[2])
    await message.delete()

    for _ in range(count):
        await client.send_message(message.chat.id, text)
        await asyncio.sleep(sleep)


@Client.on_message(filters.command("help_spam", prefixes=prefix) & filters.me)
async def help_spam(client, message):
    await message.edit(f"""```{prefix}stspam [ID] [Count] [Delay]``` - **Start sticker spam.**
```{prefix}spam [Count] [Delay] [Text]``` - **Start message spam.**""")


module_list['Spam'] = f'{prefix}spam'
file_list['Spam'] = 'spam.py'
