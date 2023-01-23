import time
import typing
import utils

from pyrogram import Client, filters
from ..plugins.settings.main_settings import module_list, file_list
from pyrogram import filters
from pyrogram.errors import UserAdminInvalid
from pyrogram.types import ChatPermissions, Message

from ..prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command('ban', prefix) & filters.me)
async def ban(client, message: Message):
    try: 
     reason = message.text.split(maxsplit=2)[1]
    except Exception:
        reason = "Not specified"
    try:
        if not message.reply_to_message:
            await message.edit(f"<b>Message must be reply to message!</b>")
            return
        await client.ban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.reply_to_message.from_user.id,
        )
        await message.edit(f"<b><code>{message.reply_to_message.from_user.first_name}</code> has been banned!</b>\n<b>Reason:</b> <i>{reason}</i>")
    except Exception:
            pass


@Client.on_message(filters.command("unban", prefix) & filters.me)
async def unban(client, message: Message):
    try:
        if message.reply_to_message:
                await client.unban_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.reply_to_message.from_user.id,
                )
                await message.edit(f"<b><code>{message.reply_to_message.from_user.first_name}</code> has been unbanned!</b>")
        if not message.reply_to_message:
            await message.edit(f"<b>Message must be reply to message!</b>")        
    except Exception:
            pass

module_list["Moderation"] = {
"ban [reply] [reason]": "Ban member",
"unban [reply]": "Unban member",
}
file_list["Moderation"] = "moderation.py"
