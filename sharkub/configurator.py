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
        print(colored('Choose userbot language [ru/en/ua]\nLeave it empty to choose default', 'white', attrs=['bold']))
        ulang = input("> ")
        if ulang == "":
            ublang = "en"
        else:
          if ulang == "ru" or ulang == "russian":
           ublang = "ru"
          elif ulang == "en" or ulang == "english":
           ublang = "en"
          elif ulang == "ua" or ulang == "ukrainian":
           ublang = "ua"
          else:
           ublang = "en"
        os.system("cls" if os.name == "nt" else "clear")
        print(colored('Enter your API_ID and API_HASH', 'white', attrs=['bold']))
        print(colored('You can get it here -> https://my.telegram.org/apps\nLeave empty to use defaults  (please note that default keys significantly increases your ban chances)', 'white', attrs=['bold']))
        config_id = input("API_ID > ")
        config_hash = input("API_HASH > ")
        if config_id == "" or config_hash == "":
            conf_id = "2040"
            conf_hash = "b18441a1ff607e10a989891a5462e627"
        else:
            conf_id = config_id
            conf_hash = config_hash
        os.system("cls" if os.name == "nt" else "clear")
        print(colored("Enter your ChatGPT token\nIf you haven't got it press ENTER", 'white', attrs=['bold']))
        gpttok = input("ChatGPT token > ")
        os.system("cls" if os.name == "nt" else "clear")
        if gpttok == "":
            gpttoken = "Your_ChatGPT_token"
        else:
            gpttoken = gpttok
        config.add_section("pyrogram")
        config.set("pyrogram", "api_id", conf_id)
        config.set("pyrogram", "api_hash", conf_hash)
        config.set("pyrogram", "device_model", config_model)
        config.add_section("ChatGPT")
        config.set("ChatGPT", "gpt_token", gpttoken)
        config.add_section("Language")
        config.set("Language", "language", ublang)
        with open("config.ini", "w") as config_file:
            config.write(config_file)

        api_id = conf_id
        api_hash = conf_hash
        device_model = config_model
    return api_id, api_hash, device_model
