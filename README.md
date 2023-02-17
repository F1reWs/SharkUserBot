<p align="center">
    <img src="https://github.com/Master-Stroke/SharkUserBot/raw/main/assets/banner.gif" width="500" alt="SharkUserBot">
    </a>
    <br>
    <b>SharkUserBot v0.0.9</b>
    <br>
    <b>Telegram userbot</b>
<br><br>

<a href="https://github.com/Master-Stroke/SharkUserBot/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/Master-Stroke/SharkUserBot?style=for-the-badge">
</a>

<a href="https://github.com/Master-Stroke/SharkUserBot/commits/main">
    <img alt="last-commit" src="https://img.shields.io/github/last-commit/Master-Stroke/SharkUserBot?style=for-the-badge">
</a>

<a href="https://github.com/Master-Stroke/SharkUserBot">
    <img alt="Stars" src="https://img.shields.io/github/stars/Master-Stroke/SharkUserBot?style=for-the-badge">
    <img alt="Size" src="https://img.shields.io/github/repo-size/Master-Stroke/SharkUserBot?style=for-the-badge">
    <img alt="Language" src="https://img.shields.io/github/languages/top/Master-Stroke/SharkUserBot?style=for-the-badge">
    <img alt="Python" src="https://img.shields.io/badge/python->=%203.8-blue?style=for-the-badge">
</a>

</p>
<hr>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Simple+and+cool+telegram+userbot)](https://t.me/Shark_UserBot)

<h1>Custom modules</h1>
<h3>Download custom modules in <a href="https://t.me/SharkUBmodules_bot">@SharkUBmodules_bot</a></h3>
<p>You can create your module in SharkUserBot!</p>

```python3
from pyrogram import Client, filters
from sharkub.settings.main_settings import module_list, file_list

from sharkub.settings.prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("example_edit", prefixes=prefix) & filters.me)
async def example_edit(client, message):
    await message.edit("<code>This is an example module</code>")

module_list["Example"] = {
"example_edit": "Description",
}
file_list["Example"] = "example.py"
```

<h1>Install and Start</h1>
<h2>How to install?</h2>


- Termux (Download termux from [this link](https://f-droid.org/repo/com.termux_118.apk).)<br>⚠️ Version from Play Store not working!

```
pkg update -y && pkg install python3 && pkg install git && pkg install libjpeg-turbo && git clone https://github.com/Master-Stroke/SharkUserBot && cd SharkUserBot && bash start.sh
```

- APT (Debian/Ubuntu based)

```
sudo apt update -y && sudo apt install python3 python3-pip && sudo apt install git && git clone https://github.com/Master-Stroke/SharkUserBot && cd SharkUserBot && bash start.sh
```

<h3>Windows/Mac OS</h2>
<h4>Install</h3>

- Install <a href="https://www.python.org/downloads/">python3</a>

- Download and Unzip <a href="https://github.com/Master-Stroke/SharkUserBot/archive/refs/heads/main.zip">This file</a>

- Write in terminal `pip install -r requirements.txt`

<h4>How to start on Windows</h3>

- Open windows.bat

<h4>How to start on Mac OS</h3>

- Type in terminal `python3 -m sharkub`
<hr>
<h1>Channel and Group</h1>
<a href="https://t.me/shark_userbot">
<img alt="Telegram" src="https://img.shields.io/badge/Telegram_Channel-0a0a0a?style=for-the-badge&logo=telegram">
</a>
<a href="https://t.me/shark_userbot_support">
<img alt="Telegram" src="https://img.shields.io/badge/Telegram_Chat-0a0a0a?style=for-the-badge&logo=telegram">
</a>
<br>
<hr>
<i>⚠️ This project is provided as-is. Developer doesn't take ANY responsibility over any problems, caused by userbot. By installing SharkUserBot you take all risks on you. Please, consider reading https://core.telegram.org/api/terms for more information.</i>
<br>
<hr>
<b>Special thanks to:</b>
<ul>
    <li><a href="https://github.com/A9FM">A9FM</a> for FoxUserBot, which is the base of project</li>
    <li><a href="https://t.me/slick_off">Slick</a> for helping in creating userbot</li>
    <li><a href="https://github.com/delivrance">Dan</a> for pyrogram, which is the base of project</li>
</ul>    
<hr>    
<h1>Developer</h1>
➤ Platon <a href="https://github.com/Master-Stroke">Github</a> | <a href="https://t.me/MasterStroke777">Telegram</a> <br>
