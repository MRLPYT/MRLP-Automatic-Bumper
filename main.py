from __future__ import absolute_import
try:
    import os
    import json
    import random
    import time
    import requests
    from time import *
    from colorama import Fore, Back, Style, init
    init()
except ImportError as ex:
    input(f"Module {ex.name} not installed, to install run '{'python' if os.name == 'nt' else 'python3'} -m pip install {ex.name}'\nPress enter to exit")
    exit()
def main():
    while True:
        try:
            for line in open("tokenlist.txt", "r"):
                token = str(line)
                try:
                    for line in open("idlist.txt", "r"):
                        id = line
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
                            print(f"Bumped! -- {id} with {token}")
                        except Exception as e:
                            print(f"\n [!] Error with the ID-List or the Request-Libary: \n {e}")
                except:
                    print("[!] File `tokenlist.txt` not found. Exiting Loop.")
                    sleep(0.8)
                    print("[!] File `tokenlist.txt` not found. Exiting Loop..")
                    sleep(0.8)
                    print("[!] File `tokenlist.txt` not found. Exiting Loop...")
                    sleep(0.8)
                    break
        except:
            print("[!] Loop is broken!")
            break
        sleep(121*60)

print(Fore.LIGHTBLUE_EX + f"""  __  __ _____  _      _____              _    _ _______ ____         ____  _    _ __  __ _____  ______ _____  
 |  \/  |  __ \| |    |  __ \        /\  | |  | |__   __/ __ \       |  _ \| |  | |  \/  |  __ \|  ____|  __ \ 
 | \  / | |__) | |    | |__) |_____ /  \ | |  | |  | | | |  | |______| |_) | |  | | \  / | |__) | |__  | |__) |
 | |\/| |  _  /| |    |  ___/______/ /\ \| |  | |  | | | |  | |______|  _ <| |  | | |\/| |  ___/|  __| |  _  / 
 | |  | | | \ \| |____| |         / ____ \ |__| |  | | | |__| |      | |_) | |__| | |  | | |    | |____| | \ \ 
 |_|  |_|_|  \_\______|_|        /_/    \_\____/   |_|  \____/       |____/ \____/|_|  |_|_|    |______|_|  \_\\
                                                                                                               """)
                                                                                                               
print("""Do you already add your Account-Token's [tokenlist.txt] and your Channel-ID's [idlist.txt]?
[1] = True
[2] = False""")
setupdone = str(input(f"[?] "))
if setupdone == "1":
    sleep(0.8)
    print("Loading.")
    sleep(0.8)
    print("Loading..")
    sleep(0.8)
    print("Loading...")
    sleep(0.8)
    print("Done!")
    sleep(0.8)
    main()
elif setupdone == "2":
    print("Please configure the Bot first.")
    sleep(1)
    print("System will Exit in 5 Seconds!")
    sleep(1)
    print("System will Exit in 4 Seconds!")
    sleep(1)
    print("System will Exit in 3 Seconds!")
    sleep(1)
    print("System will Exit in 2 Seconds!")
    sleep(1)
    print("System will Exit in 1 Seconds!")
    sleep(1)
    print("System will Exit in 0 Seconds!")
    sleep(1)
    print("[!] System quited!")
    exit
else:
    print("Input-Error [1] / [2] - System will Exit in 5 Seconds!")
    sleep(1)
    print("Input-Error [1] / [2] - System will Exit in 4 Seconds!")
    sleep(1)
    print("Input-Error [1] / [2] - System will Exit in 3 Seconds!")
    sleep(1)
    print("Input-Error [1] / [2] - System will Exit in 2 Seconds!")
    sleep(1)
    print("Input-Error [1] / [2] - System will Exit in 1 Seconds!")
    sleep(1)
    print("Input-Error [1] / [2] - System will Exit in 0 Seconds!")
    sleep(1)
    print("[!] System quited!")
    exit