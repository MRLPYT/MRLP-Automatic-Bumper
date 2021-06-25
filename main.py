from __future__ import absolute_import
try:
    import os
    import json
    import time
    import requests
    from time import *
    from colorama import Fore, Back, Style, init
    init()
except ImportError as ex:
    input(f"Module {ex.name} not installed, to install run '{'python' if os.name == 'nt' else 'python3'} -m pip install {ex.name}'\nPress enter to exit")
    exit()

print(Fore.LIGHTBLUE_EX + f"""  __  __ _____  _      _____              _    _ _______ ____         ____  _    _ __  __ _____  ______ _____  
 |  \/  |  __ \| |    |  __ \        /\  | |  | |__   __/ __ \       |  _ \| |  | |  \/  |  __ \|  ____|  __ \ 
 | \  / | |__) | |    | |__) |_____ /  \ | |  | |  | | | |  | |______| |_) | |  | | \  / | |__) | |__  | |__) |
 | |\/| |  _  /| |    |  ___/______/ /\ \| |  | |  | | | |  | |______|  _ <| |  | | |\/| |  ___/|  __| |  _  / 
 | |  | | | \ \| |____| |         / ____ \ |__| |  | | | |__| |      | |_) | |__| | |  | | |    | |____| | \ \ 
 |_|  |_|_|  \_\______|_|        /_/    \_\____/   |_|  \____/       |____/ \____/|_|  |_|_|    |______|_|  \_\\
                                                                                                               
                                                                                                               
Coded by Mr Let's Play
YouTube: @Mr Let's Play
Twitter: @JorisJanke
Instagram: @Jorisdelme
TikTok: @mrlp.tiktok
""")
print(f" {Fore.CYAN}\n \n [!] Please enter your Account-Token:")
token = input(f"{Fore.BLUE}>> ")
print("\n [!] Please enter your Channel-ID:")
id = input(f"{Fore.BLUE}>>")
while True:
    try:
        headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Authorization' : token
        }
        requests.post(
        f"https://discord.com/api/channels/{id}/messages",
        headers = headers,
        json = {"content" : "!d bump"}
        )
        print(f"{Fore.GREEN}Bumped! -- {id} with {token}")
    except Exception as e:
        print(f"\n [!] Error with the ID or the Request-Libary: \n {e}")
    sleep(121*60)
