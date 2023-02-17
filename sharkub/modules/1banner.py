#    SharkUB (telegram userbot by https://github.com/Master-Stroke)
#    Copyright (C) 2023 SharkUserBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    GNU General Public License https://www.gnu.org/licenses.

import os
from rich import print
from ..settings.main_settings import version

from ..settings.prefix import my_prefix
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

SharkUserBot [green]Started[/green]
Type [purple]{prefix}ping[/purple] to check Userbot works[/blue]""")
