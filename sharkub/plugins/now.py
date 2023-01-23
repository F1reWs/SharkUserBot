import asyncio
from ..plugins.settings.main_settings import module_list, file_list
from pyrogram import Client , filters
import requests , time
import datetime

from ..prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("now", prefixes=prefix) & filters.me)
async def today(client , message):
    weekday = datetime.datetime.today().weekday()
    if weekday == 0:
        today = "monday"
    elif weekday == 1:
        today = "tuesday"
    elif weekday == 2:
        today = "wednesday"
    elif weekday == 3:
        today = "thursday"
    elif weekday == 4:
        today = "friday"
    elif weekday == 5:
        today = "saturday"
    elif weekday == 6:
        today = "sunday"

    hour = int(datetime.datetime.today().strftime("%H")) % 10
    minute = int(datetime.datetime.today().strftime("%M")) % 10
    hour_s = "часа"
    minute_s = "минут"

    if hour == 1:
        hour_s = "hour"
    elif hour >=2 and hour <= 4:
        hour_s = "hours"
    else:
        hour_s = "hours"

    if minute == 1:
        minute_s = "minute"
    elif minute >= 2 and minute <=4:
        minute_s = "minutes"
    else:
        minute_s = "minute"


    text = f"""**Today** `{today}`, **on calendar** `{datetime.datetime.today().strftime("%d.%m.%Y")}`
**Now** `{int(datetime.datetime.today().strftime("%j"))}` **day** `{datetime.datetime.today().strftime("%Y")}` **year**
**Now time** `{datetime.datetime.today().strftime("%H")}` {hour_s} `{datetime.datetime.today().strftime("%M")}` {minute_s} """
    await message.edit(text)


module_list["Now"] = {
    "now": "Show now date and time",
}
file_list["Now"] = "now.py"