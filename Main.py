#!/usr/bin/env python3
import os
import time

# ANSI رنګونه
RED_BG = "\033[41m"
WHITE_TEXT = "\033[97m"
RESET = "\033[0m"
GREEN_TEXT = "\033[1;32m"

logo = '''
[+]
| ███████╗ █████╗ █████╗░░░██████╗  ██████╗░░░██████╗░░░░░░░░░░██╗███╗░░██╗░█████╗░░░░░  
| ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗ ██╔═══██╗░░░░░░░░░██║████╗░██║██╔══██╗░░░░ 
| █████╗░ ███████║██████╔╝██║░░░██║██║░░░██║ ██║░░░██║░██████╗░██║██╔██╗██║██║░░╚═╝░░░░ 
| ██╔══╝░ ██╔══██║██╔══██╗██║░░░██║██║░░░██║ ██║▄▄░██║░╚═════╝░██║██║╚████║██║░░██╗░░░░  
| ██║░░░░ ██║░░██║██║░░██║╚██████╔╝╚██████╔╝░╚██████╔╝░░░░░░░░░██║██║░╚███║╚█████╔╝░░░░  
| ╚═╝░░░░ ╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚═════╝░░░╚══▀▀═╝░░░░░░░░░░╚═╝╚═╝░░╚══╝░╚════╝░░░░░  V2.7

[+] Title    : AllHackingTools - Tool for hacking  -  ATTENTION! The author of this article is not respo-
[+] Github   : https://github.com/mishakorzik  -  nsible responsible for any consequences of reading it. 
[+] Coded By : Misha Korzhik (Міша Коржик)  -  All materials are provided for educational purposes only! 
[+]-------+---------+---------+---------+---------+---------+---------+---------+-------[+]

[01] Quick Start - on/off
[02] Servers Setting
[03] Extra Keys
[04] Add to Startup
[05] System Process Viewer
[06] Exit Tool
'''

def clear():
    os.system("clear")

def print_red_bg(text):
    """د سور شالید سره متن چاپول"""
    print(f"{RED_BG}{WHITE_TEXT}{text}{RESET}")

def banner():
    # که lolcat نصب دی، نو د سور شالید سره به ښه نه ښکاري
    # نو دوه انتخابونه:
    
    # انتخاب 1: یوازې د سور شالید سره (بې lolcat)
    for line in logo.split('\n'):
        if line.strip():
            print_red_bg(line)
        else:
            print()
    
    # انتخاب 2: که lolcat وساتئ، نو سور شالید به اغیزمن نه وي
    # os.system(f"echo \"{logo}\" | lolcat")

def welcome():
    print(f"{GREEN_TEXT}Welcome to FAROOQ Tool...{RESET}")
    time.sleep(1)

def main():
    clear()
    welcome()
    time.sleep(0.5)
    clear()
    banner()

if __name__ == "__main__":
    main() 
