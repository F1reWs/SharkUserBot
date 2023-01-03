import asyncio
from plugins.settings.main_settings import module_list, file_list
from pyrogram import Client , filters
import requests , time
import datetime

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("now", prefixes=prefix) & filters.me)
async def today(client , message):
    weekday = datetime.datetime.today().weekday()
    if weekday == 0:
        today = "понедельник"
    elif weekday == 1:
        today = "вторник"
    elif weekday == 2:
        today = "среда"
    elif weekday == 3:
        today = "четверг"
    elif weekday == 4:
        today = "пятница"
    elif weekday == 5:
        today = "суббота"
    elif weekday == 6:
        today = "воскресенье"

    hour = int(datetime.datetime.today().strftime("%H")) % 10
    minute = int(datetime.datetime.today().strftime("%M")) % 10
    hour_s = "часа"
    minute_s = "минут"

    if hour == 1:
        hour_s = "час"
    elif hour >=2 and hour <= 4:
        hour_s = "часа"
    else:
        hour_s = "часов"

    if minute == 1:
        minute_s = "минута"
    elif minute >= 2 and minute <=4:
        minute_s = "минуты"
    else:
        minute_s = "минут"


    text = f"""**Сегодня** `{today}`, **на календаре** `{datetime.datetime.today().strftime("%d.%m.%Y")}`
**Идёт** `{int(datetime.datetime.today().strftime("%j"))}` **день** `{datetime.datetime.today().strftime("%Y")}` **года**
**Текущее время** `{datetime.datetime.today().strftime("%H")}` {hour_s} `{datetime.datetime.today().strftime("%M")}` {minute_s} """
    await message.edit(text)


module_list['Now'] = f'{prefix}now'
file_list['Now'] = 'now.py'
