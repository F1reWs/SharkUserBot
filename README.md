<p align="center">
    <img src="https://github.com/Master-Stroke/SharkUserBot/raw/main/SharkUserBot.png" width="500" alt="SharkUserBot">
    </a>
    <br>
    <b>SharkUserBot</b>
    <br>
    <b>Telegram userbot</b>
<br><br>

<a href="https://github.com/Master-Stroke/SharkUserBot/commits/main">
    <img alt="last-commit" src="https://img.shields.io/github/last-commit/Master-Stroke/SharkUserBot?style=for-the-badge">
</a>

<a href="https://github.com/Master-Stroke/SharkUserBot">
    <img alt="Stars" src="https://img.shields.io/github/stars/Master-Stroke/SharkUserBot?style=for-the-badge">
    <img alt="Size" src="https://img.shields.io/github/repo-size/Master-Stroke/SharkUserBot?style=for-the-badge">
    <img alt="Language" src="https://img.shields.io/github/languages/top/Master-Stroke/SharkUserBot?style=for-the-badge">
    <img alt="Python" src="https://img.shields.io/badge/python->=%203.7-blue?style=for-the-badge">
</a>

</p>

<h1>Custom modules</h1>

<p>You can create your module in SharkUserBot!</p>

```python3
from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("example_edit", prefixes=prefix) & filters.me)
async def example_edit(client, message):
    await message.edit("<code>This is an example module</code>")
    
module_list['Example'] = f'{prefix}example_edit'
file_list['Example'] = 'example.py'
```

<h1>Install and Start</h1>
<h2>How to install?</h2>


- Termux

```
pkg update -y && pkg install python3 wget -y && pkg install git && termux-wake-lock && git clone https://github.com/Master-Stroke/SharkUserBot && cd SharkUserBot-main && pip3 install -r requirements.txt && python3 main.py)
```

- APT (Debian based)


```
apt update -y && sudo apt install python3 python3-pip wget -y && wget -O foxub.$$ https://github.com/Master-Stroke/SharkUserBot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd SharkUserBot-main && pip3 install -r requirements.txt && python3 main.py)
```

- YUM (RHEL based)

```
yum -y update && sudo yum install wget python3 curl -y && python3 <(curl -sSL https://bootstrap.pypa.io/get-pip.py) && wget -O foxub.$$ https://github.com/Master-Stroke/SharkUserBot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd SharkUserBot-main && pip3 install -r requirements.txt && python3 main.py)
```

- PACMAN (Arch based)

```
sudo pacman -Sy python3 wget curl && python3 <(curl -sSL https://bootstrap.pypa.io/get-pip.py) && wget -O foxub.$$ https://github.com/Master-Stroke/SharkUserBot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd SharkUserBot-main && pip3 install -r requirements.txt && python3 main.py)
```

- EMERGE (Gentoo)
```
sudo emerge python wget net-misc/curl && python3 <(curl -sSL https://bootstrap.pypa.io/get-pip.py) && wget -O foxub.$$ https://github.com/Master-Stroke/SharkUserBot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm -rf foxub.$$ && cd SharkUserBot-main && pip3 install -r requirements.txt && python3 main.py)
```

- MacOS

```
xcode-select --install ; /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" && brew install python3 && pip3 install --upgrade pip && pip3 install wheel && brew install wget && wget -O foxub.$$ https://github.com/Master-Stroke/SharkUserBot/archive/refs/heads/main.zip && (unzip foxub.$$ && rm foxub.$$ && cd SharkUserBot-main && pip3 install -r requirements.txt && python3 main.py)
```

<h3>Windows</h2>
<h4>Install</h3>

- Install <a href="https://www.python.org/downloads/">python3</a>

- Download and Unzip <a href="https://github.com/Master-Stroke/SharkUserBot/archive/refs/heads/main.zip">This file</a>

- Write in CMD `pip install -r requirements.txt`

<h4>How to start</h3>

- Open windows.bat

<h1>Channel and Group</h1>
<a href="https://t.me/shark_userbot">
<img alt="Telegram" src="https://img.shields.io/badge/Telegram_Channel-0a0a0a?style=for-the-badge&logo=telegram">
</a>
<a href="https://t.me/shark_userbot_support">
<img alt="Telegram" src="https://img.shields.io/badge/Telegram_Chat-0a0a0a?style=for-the-badge&logo=telegram">
</a>
    
<h1>Developer</h1>
➤ Platon <a href="https://github.com/Master-Stroke">Github</a> | <a href="https://t.me/MasterStroke777">Telegram</a> <br>
 
