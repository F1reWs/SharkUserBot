import logging
import os

def logger():
    logging.basicConfig(
        filename="temp/shark_userbot.log",
        filemode="w",
        format="%(asctime)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        level=logging.INFO
    )

def userbot():
    from pyrogram import Client
    from . import configurator
    from . import prestarter
    api_id, api_hash, device_mod = configurator.my_api()
    prestarter.prestart(api_id, api_hash, device_mod)
    Client = Client(
        "my_account",
        api_id=api_id,
        api_hash=api_hash,
        device_model=device_mod,
        plugins=dict(root="sharkub/modules")
    ).run()
    
if __name__ == "__main__":
    userbot()
    logger()