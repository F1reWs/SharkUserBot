from pyrogram import Client, filters
import sys
import os
import time
import pip

def prestart(api_id, api_hash, device_mod):
    app = Client("my_account", api_id=api_id, api_hash=api_hash, device_model=device_mod)
    with app:
        if len(sys.argv) == 4:
            restart_type = sys.argv[3]
            requirements = [
                "install",    
                "pyrogram",
                "wheel",
                "utils",
                "telegraph",
                "requests",
                "wget",
                "rich",
                "wikipedia",
                "gTTS",
                "datetime",
                "qrcode",
                "speedtest-cli",
                "psutil",
                "pillow",
                "termcolor"
                ]
            if restart_type == "1":
                pip.main(requirements)
                text = "<code>Update process completed!</code>"
            else:
                pip.main(requirements)
                text = "**Userbot succesfully Restarted**"
            try:
                app.send_message(int(sys.argv[1]), text)
            except Exception as f:
                app.send_message("me", f"Got error: {f}\n\n" + text)
                pass

        app.join_chat("shark_userbot")
        time.sleep(1)
        app.join_chat("shark_userbot_support")
