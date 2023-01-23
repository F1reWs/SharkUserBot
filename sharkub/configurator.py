import os
import sys
import configparser
from termcolor import colored

config_model = "SharkUserBot"

config = configparser.ConfigParser()
config.read("config.ini")


def api():
    get_id = config.get("pyrogram", "api_id")
    get_hash = config.get("pyrogram", "api_hash")
    get_device_model = config.get("pyrogram", "device_model")
    return get_id, get_hash, get_device_model


def my_api():
    try:
        api_id, api_hash, device_model = api()
    except:
        os.system("cls" if os.name == "nt" else "clear")
      #  print(f"Not found config.ini\nGenerating new...")        
        config.add_section("pyrogram")
        print(colored('Enter your API_ID and API_HASH', 'white', attrs=['bold']))
        print(colored('You can get it here -> https://my.telegram.org/apps', 'white', attrs=['bold']))
        config_id = input("API_ID > ")
        config.set("pyrogram", "api_id", config_id)
        config_hash = input("API_HASH > ")
        config.set("pyrogram", "api_hash", config_hash)
        config.set("pyrogram", "device_model", config_model)
        with open("config.ini", "w") as config_file:
            config.write(config_file)

        api_id = config_id
        api_hash = config_hash
        device_model = config_model
    return api_id, api_hash, device_model
