from pyrogram import Client, filters
from pyrogram.errors.exceptions.flood_420 import FloodWait
from plugins.settings.main_settings import module_list, file_list
from collections import deque
import asyncio
import random

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("hack", prefix) & filters.me)
async def hack(client, message):
    perc = 0
    while perc < 100:
        text = "👮 Взлом пентагона в процессе..." + str(perc) + "%"
        await message.edit(str(text))
        perc += random.randint(1, 3)
        await asyncio.sleep(0.1)
    text = "✅ Пентагон успешно взломан!"
    await message.edit(str(text))
    await asyncio.sleep(3)
    perc = 0
    while perc < 100:
        text = "⬇️ Скачивание данных..." + str(perc) + "%"
        await message.edit(str(text))
        perc += random.randint(1, 5)
        await asyncio.sleep(0.15)
    await asyncio.sleep(1)
    text = "🐓 Нашли файлы что ты петух!"
    await message.edit(text)


@Client.on_message(filters.command("drugs", prefix) & filters.me)
async def drugs(client, message):
    perc = 0
    while perc < 100:
        text = "💊 Поиск запрещённых препаратов " + str(perc) + "%"
        await message.edit(str(text))
        perc += random.randint(1, 3)
        await asyncio.sleep(0.1)
    text = "🚬 Найдено 3 кг шпекса"
    await message.edit(str(text))
    await asyncio.sleep(3)
    text = "🌿⚗️ Оформляем вкид"
    await message.edit(str(text))
    await asyncio.sleep(5)
    drugsss = ['😳 Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты',
               '🥴 Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте  ещё раз оформить вкид',
               '😖 Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз',
               '😌 Вы оформили вкид, Вам понравилось']
    drug = random.choice(drugsss)
    await message.edit(drug)


@Client.on_message(filters.command("police", prefix) & filters.me)
async def police(client, message):
    red_blue = "🔴🔴🔴⬜⬜⬜🔵🔵🔵"
    blue_red = "🔵🔵🔵⬜⬜⬜🔴🔴🔴"
    duration = 0
    try:
        need_duration = int(message.command[1])
    except:
        need_duration = 5
    while need_duration != duration:
        await message.edit(f"{red_blue}\n" * 3)
        await asyncio.sleep(0.3)
        await message.edit(f"{blue_red}\n" * 3)
        await asyncio.sleep(0.3)
        duration += 1
    await message.edit("**Никому ни с места!**\nПрибыла **🚨 Полиция 🚨**\nГотовь вещички, **сынок**.")


# Переменные с кастомом
end_message = '**1000-7, я умер, прости**'
messages_per_second = 7
sleep_time_ghoul = 0.1


@Client.on_message(filters.command("ghoul", prefixes=prefix) & filters.me)
async def ghoul_spam_handler(client, message):
    i = 1000
    while i > 0:
        try:
            await client.send_message(message.chat.id, f'{i} - 7 = {i-7}')
        except FloodWait as e:
            await asyncio.sleep(e.value)

        i -= 7
        await asyncio.sleep(1/messages_per_second)

    if end_message != '':
        await client.send_message(message.chat.id, end_message)


@Client.on_message(filters.command("stupid", prefix) & filters.me)
async def stupid(client, message):
    animation_interval = 0.5
    animation_ttl = range(0, 14)
    await message.edit_text("stupid boy")
    animation_chars = [
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n🧠         (^_^)🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n🧠       (^_^)  🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n🧠     (^_^)    🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n🧠   (^_^)      🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n🧠 (^_^)        🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n🧠< (^_^ <)         🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n           (> ^_^)>🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n           < (^_^ <)🗑",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit_text(animation_chars[i % 14])


@Client.on_message(filters.command("bombs", prefix) & filters.me)
async def bombs(client, message):
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await message.edit_text("<b>RIP DOMBASS......</b>")
    await asyncio.sleep(2)


@Client.on_message(filters.command("call", prefix) & filters.me)
async def cell(client, message):
    animation_interval = 3
    animation_ttl = range(0, 18)
    await message.edit_text("Calling Pavel Durov (ceo of telegram)......")
    animation_chars = [
        "<b>Connecting To Telegram Headquarters...</b>",
        "<b>Call Connected.</b>",
        "<b>Telegram: Hello This is Telegram HQ. Who is this?</b>",
        f"<b>Me: Yo this is FoxU ,Please Connect me to my lil bro,Pavel Durov </b>",
        "<b>User Authorised.</b>",
        "<b>Calling Shivamani </b>  <code>At +916969696969</code>",
        "<b>Private  Call Connected...</b>",
        "<b>Me: Hello Sir, Please Ban This Telegram Account.</b>",
        "<b>Shivamani : May I Know Who Is This?</b>",
        f"<b>Me: Yo Brah, I Am FoxU</b>",
        "<b>Shivamani : OMG!!! Long time no see, Wassup cat...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.</b>",
        "<b>Me: Thanks, See You Later Brah.</b>",
        "<b>Shivamani : Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.</b>",
        "<b>Me: Is There Any Issue/Emergency???</b>",
        "<b>Shivamani : Yes Sur, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.</b>",
        "<b>Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.</b>",
        "<b>Shivamani : Sure Sur \nTC Bye Bye :)</b>",
        "<b>Private Call Disconnected.</b>",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit_text(animation_chars[i % 18])


@Client.on_message(filters.command("kill", prefix) & filters.me)
async def kill(client, message):
    animation_interval = 0.3
    animation_ttl = range(0, 103)
    animation_chars = [
        "Ｆｉｉｉｉｉｒｅ",
        "(　･ิω･ิ)︻デ═一-->",
        "---->____________"
        "------>__________",
        "-------->",
        "---------->",
        "------------>",
        "-------------->",
        "------------------>",
        "------>;(^。^)ノ",
        "(￣ー￣) DED",
        "<b>Target killed successfully (°̥̥̥̥̥̥̥̥•̀.̫•́°̥̥̥̥̥̥̥)</b>",
    ]

    await message.edit_text("You're goonnaa diieeeee!")
    await asyncio.sleep(3)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit_text(animation_chars[i % 103])


module_list['Troll'] = f'{prefix}hack | {prefix}drugs | {prefix}police | {prefix}ghoul | {prefix}stupid | {prefix}bombs | {prefix}call | {prefix}kill'
file_list['Troll'] = 'troll.py'
