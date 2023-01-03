import os
from rich import print
from plugins.settings.main_settings import version

from prefix import my_prefix
prefix = my_prefix()

os.system("cls" if os.name == "nt" else "clear")
print(f"""[blue]
 ____  _                _    _   _               ____        _   
/ ___|| |__   __ _ _ __| | _| | | |___  ___ _ __| __ )  ___ | |_ 
\___ \| '_ \ / _` | '__| |/ / | | / __|/ _ \ '__|  _ \ / _ \| __|
 ___) | | | | (_| | |  |   <| |_| \__ \  __/ |  | |_) | (_) | |_ 
|____/|_| |_|\__,_|_|  |_|\_\\___/|___/\___|_|  |____/ \___/ \__|

[/blue][blue]
Version: [purple]{version}[/purple]
Prefix: [[purple]{prefix}[/purple]]

Client [green]Started[/green]
Type [purple]{prefix}ping[/purple] to check Userbot works[/blue]""")
