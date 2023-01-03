import asyncio
import datetime
from pyrogram import Client, filters, types
from plugins.settings.main_settings import module_list, file_list


from prefix import my_prefix
prefix = my_prefix()

afk_info = {
    "start": datetime.datetime.now(),
    "is_afk": False,
    "reason": "",
}

is_afk = filters.create(lambda _, __, ___: afk_info["is_afk"])


@Client.on_message(is_afk & ~filters.me & ((filters.private & ~filters.bot) | (filters.mentioned & filters.group)))
async def afk_handler(_, message: types.Message):
    end = datetime.datetime.now().replace(microsecond=0)
    afk_time = end - afk_info["start"]
    await message.reply_text(
        f"❕ This user <b>AFK</b>.\n💬 Reason:</b> <i>{afk_info['reason']}</i>\n<b>⏳ Duration:</b> {afk_time}"
    )


@Client.on_message(filters.command("afk", prefix) & filters.me)
async def afk(_, message):
    if len(message.text.split()) >= 2:
        reason = message.text.split(" ", maxsplit=1)[1]
    else:
        reason = "None"

    afk_info["start"] = datetime.datetime.now().replace(microsecond=0)
    afk_info["is_afk"] = True
    afk_info["reason"] = reason

    await message.edit(f"❕ I'm going <b>AFK</b>.\n<b>💬 Reason:</b> <i>{reason}</i>.")


@Client.on_message(filters.command("unafk", prefix) & filters.me)
async def unafk(_, message):
    if afk_info["is_afk"]:
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = end - afk_info["start"]
        await message.edit(f"<b>❕ I'm not <b>AFK</b> anymore.\n" f"⏳ I was <b>AFK:</b> {afk_time}")
        afk_info["is_afk"] = False
    else:
        await message.edit("<b>❌ You weren't afk</b>")


module_list['AFK'] = f'{prefix}afk | {prefix}unafk'
file_list['AFK'] = 'afk.py'
