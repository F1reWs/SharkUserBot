from pyrogram import Client, filters
from pyrogram.types import Message
from ..settings.main_settings import module_list, file_list

from ..settings.prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("userinfo", prefixes=prefix) & filters.me)
async def get_full_user_inf(client: Client, message: Message):
    await message.edit("<code>Receiving the information...</code>")

    if len(message.text.split()) >= 2:
        try:
            user = message.text.split()[1]
            user = int(user)
        except:
            try:
                user = message.reply_to_message.from_user.id
            except:
                user = message.from_user.id
    else:
        try:
            user = message.reply_to_message.from_user.id
        except:
            user = message.from_user.id

    try:
        user_info = await client.get_users(user)

        try:
            username = f"@{user_info.username}"
        except:
            username = "None"

        user_info = f"""==========
[$] Username: <b>{username}</b>
[$] Mention: <b>{user_info.mention}</b>
[$] Id: <code>{str(user_info.id)}</code>
[$] Bot: <code>{str(user_info.is_bot)}</code>
[$] Scam: <code>{str(user_info.is_scam)}</code>
[$] Name: <code>{str(user_info.first_name)}</code>
[$] Deleted: <code>{str(user_info.is_deleted)}</code>
[$] Contact: <code>{str(user_info.is_contact)}</code>
[$] Mutual contact: <code>{str(user_info.is_mutual_contact)}</code>
[$] Verified: <code>{str(user_info.is_verified)}</code>
[$] DC: <code>{str(user_info.dc_id)}</code>"""
        await message.edit(user_info)
    except Exception as f:
        await message.edit(f"**An error occured...**\n\n{f}")


module_list["UserInfo"] = {
"userinfo [reply/username/userid]": "Show information about user",
}
file_list["UserInfo"] = "user_info.py"