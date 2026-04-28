#!/usr/bin/env python3
import os
import time
import sys

# ANSI رنګونه د متن لپاره
WHITE_TEXT = "\033[97m"
BOLD = "\033[1m"
RESET = "\033[0m"
UNDERLINE = "\033[4m"

# د بکس لاینونو لپاره رنګونه (طلایی او سرو زرو رنګونه)
GOLD_LINE = "\033[38;2;255;215;0m"      # طلایی (Gold)
DARK_GOLD = "\033[38;2;184;134;11m"     # تیاره طلایی (Dark Goldenrod)
LIGHT_GOLD = "\033[38;2;255;223;0m"     # روښانه طلایی
RED_GOLD = "\033[38;2;255;69;0m"        # سور-طلایی

# د بکس شالید لپاره رنګونه - اصلي شالید
BOX1_BG = "\033[48;2;139;69;19m"        # SaddleBrown
BOX2_BG = "\033[48;2;0;100;80m"         # Teal

# د لومړي بکس لپاره ځانګړي رنګونه
SPECIAL_BG1_2 = "\033[48;2;255;102;106m"   # #ff666a (دویمه کرښه)
SPECIAL_BG1_6 = "\033[48;2;84;0;0m"        # #540000 (اخري کرښه)

# د دویم بکس لپاره ځانګړي رنګونه
SPECIAL_BG2_2 = "\033[48;2;255;177;153m"   # #ffb199 (دویمه کرښه)
SPECIAL_BG2_6 = "\033[48;2;84;0;0m"        # #540000 (اخري کرښه)

# د لومړي بکس لپاره نور رنګونه (د 1، 3، 5 کرښو لپاره)
BOX1_COLORS = [
    "\033[48;2;155;0;81m",    # #9b0051 (لومړۍ کرښه)
    SPECIAL_BG1_2,             # #ff666a (دویمه کرښه)
    "\033[48;2;255;177;153m",  # #ffb199 (دریمه کرښه)
    "\033[48;2;84;255;153m",   # #54ff99 (څلورمه کرښه)
    BOX1_BG,                   # SaddleBrown (پنځمه کرښه)
    SPECIAL_BG1_6              # #540000 (شپږمه کرښه)
]

# د دویم بکس لپاره نور رنګونه (د 1، 3، 5 کرښو لپاره)
BOX2_COLORS = [
    "\033[48;2;155;0;81m",     # #9b0051 (لومړۍ کرښه)
    SPECIAL_BG2_2,              # #ffb199 (دویمه کرښه)
    "\033[48;2;255;102;106m",  # #ff666a (دریمه کرښه)
    "\033[48;2;84;255;153m",   # #54ff99 (څلورمه کرښه)
    BOX2_BG,                   # Teal (پنځمه کرښه)
    SPECIAL_BG2_6              # #540000 (شپږمه کرښه)
]

# د متن هایلایټ رنګونه
BOX2_TEXT_HIGHLIGHT = "\033[38;2;255;215;0m"  # د متن لپاره طلایی

# د کرښو لپاره ځانګړي رنگین کوډونه
LINE_BOLD = "\033[1m"

# د پرامپټ درې مختلف رنګونه - د ❯ نښو لپاره
RED_ARROW = "\033[91m"      # سور رنګ
GREEN_ARROW = "\033[92m"    # شین رنګ
BLUE_ARROW = "\033[94m"     # نیلي رنګ

logo = '''

 ███████╗ █████╗ █████╗░░░██████╗  ██████╗░░░██████╗░░░░░░░░░░██╗███╗░░██╗░█████╗░░░░░  
 ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗ ██╔═══██╗░░░░░░░░░██║████╗░██║██╔══██╗░░░░ 
 █████╗░ ███████║██████╔╝██║░░░██║██║░░░██║ ██║░░░██║░██████╗░██║██╔██╗██║██║░░╚═╝░░░░ 
 ██╔══╝░ ██╔══██║██╔══██╗██║░░░██║██║░░░██║ ██║▄▄░██║░╚═════╝░██║██║╚████║██║░░██╗░░░░  
 ██║░░░░ ██║░░██║██║░░██║╚██████╔╝╚██████╔╝░╚██████╔╝░░░░░░░░░██║██║░╚███║╚█████╔╝░░░░  
 ╚═╝░░░░ ╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚═════╝░░░╚══▀▀═╝░░░░░░░░░░╚═╝╚═╝░░╚══╝░╚════╝░░░░░  V2.7

'''

def get_terminal_width():
    """د ترمینل عرض ترلاسه کول"""
    try:
        return os.get_terminal_size().columns
    except:
        return 80

def print_centered_big(text):
    """متن د سنټر او لوی سایز سره چاپول - دوه چنده لوی"""
    terminal_width = get_terminal_width()
    
    big_text = ""
    for char in text:
        if char.isupper() or char.islower() or char.isdigit():
            big_text += char + " "
        else:
            big_text += char
    
    if len(big_text) > terminal_width - 4:
        big_text = text
    
    text_length = len(big_text)
    padding = (terminal_width - text_length) // 2
    if padding < 0:
        padding = 0
    
    spaces = " " * padding
    mid = len(big_text) // 2
    first_half = big_text[:mid]
    second_half = big_text[mid:]
    
    print(f"{spaces}", end="")
    print(f"\033[41m\033[97m{BOLD}{UNDERLINE}{first_half}{RESET}", end="")
    print(f"\033[42m\033[97m{BOLD}{UNDERLINE}{second_half}{RESET}")

def clear():
    os.system("clear")

def banner():
    os.system(f"echo \"{logo}\" | lolcat -p 1.6")

def print_box1():
    """لومړی بکس - هر کرښه ځانګړی رنګ"""
    width = get_terminal_width()
    line_width = min(width - 4, 70)
    
    # پورتنۍ کرښه - هنري
    print(f"{LINE_BOLD}{DARK_GOLD}═══════════════════════ {GOLD_LINE}» ───── «◊•» ✠ • ◊ «─────» «═══════════════════{RESET}")
    
    # د معلوماتو کرښې
    info_lines = [
        f"  {GOLD_LINE}Developer   >>{WHITE_TEXT} Faroooq Inc",           # کرښه 1
        f"  {GOLD_LINE}Tool Type   >>{WHITE_TEXT} FILExRANDOM",           # کرښه 2
        f"  {GOLD_LINE}Github      >>{WHITE_TEXT} github.com/porn-404",   # کرښه 3
        f"  {GOLD_LINE}Version     >>{WHITE_TEXT} V2.7",                  # کرښه 4
        f"  {GOLD_LINE}Status      >>{WHITE_TEXT} Active",                # کرښه 5
        f"  {GOLD_LINE}Platform    >>{WHITE_TEXT} Termux"                 # کرښه 6
    ]
    
    for i, info in enumerate(info_lines):
        # د کرښې نمبر مطابق شالید ټاکل
        bg_color = BOX1_COLORS[i] if i < len(BOX1_COLORS) else BOX1_BG
        
        clean_info = info.replace(GOLD_LINE, '').replace(WHITE_TEXT, '').replace(RESET, '')
        info_len = len(clean_info)
        padding_needed = line_width - info_len - 4
        if padding_needed < 0:
            padding_needed = 0
        print(f"{bg_color}{WHITE_TEXT}{BOLD}║{info}{' ' * padding_needed} ║{RESET}")
    
    # ښکته کرښه - هنري
    print(f"{LINE_BOLD}{DARK_GOLD}═══════════════ ──•◆•── ────────────────•✦•───────────────────╝{RESET}")

def print_box2():
    """دویم بکس - هر کرښه ځانګړی رنګ"""
    width = get_terminal_width()
    line_width = min(width - 4, 70)
    
    # پورتنۍ کرښه - هنري
    print(f"{LINE_BOLD}{LIGHT_GOLD}═══════════════════════ {RED_GOLD}» ───── «◊•» ✠ • ◊ «─────» «═══════════════════{RESET}")
    
    # د معلوماتو کرښې
    info_lines = [
        f"  {WHITE_TEXT}Operator        >> {BOX2_TEXT_HIGHLIGHT}0171{WHITE_TEXT}",           # کرښه 1
        f"  {WHITE_TEXT}Total Account   >> {BOX2_TEXT_HIGHLIGHT}5000{WHITE_TEXT}",           # کرښه 2
        f"  {WHITE_TEXT}⚡ Use Airplane (Flight) Mode For Speed Up",                         # کرښه 3
        f"  {WHITE_TEXT}[!] {BOX2_TEXT_HIGHLIGHT}Turn on Flight Mode{WHITE_TEXT}",          # کرښه 4
        f"  {WHITE_TEXT}Speed           >> {BOX2_TEXT_HIGHLIGHT}MAXIMUM{WHITE_TEXT}",       # کرښه 5
        f"  {WHITE_TEXT}Connection      >> {BOX2_TEXT_HIGHLIGHT}STABLE{WHITE_TEXT}"         # کرښه 6
    ]
    
    for i, info in enumerate(info_lines):
        # د کرښې نمبر مطابق شالید ټاکل
        bg_color = BOX2_COLORS[i] if i < len(BOX2_COLORS) else BOX2_BG
        
        clean_info = info.replace(BOX2_TEXT_HIGHLIGHT, '').replace(WHITE_TEXT, '').replace(RESET, '')
        info_len = len(clean_info)
        padding_needed = line_width - info_len - 4
        if padding_needed < 0:
            padding_needed = 0
        print(f"{bg_color}{BOX2_TEXT_HIGHLIGHT}{BOLD}║{info}{' ' * padding_needed} ║{RESET}")
    
    # ښکته کرښه - هنري
    print(f"{LINE_BOLD}{LIGHT_GOLD}═══════════════ ──•◆•── ────────────────•✦•───────────────────╝{RESET}")

def show_prompt():
    """ترمینل پرامپټ - درې مختلف رنګونه لرونکې ❯❯❯ نښې"""
    print(f"\n\033[93m{BOLD}┌─[h4ck3r@termux]-[~]\033[0m")
    print(f"{BOLD}{RED_ARROW}└──╼{RESET} {BOLD}{RED_ARROW}❯{RESET}{BOLD}{GREEN_ARROW}❯{RESET}{BOLD}{BLUE_ARROW}❯{RESET} \033[0m", end="")

def welcome():
    """د ویلکم مسیج - لوی سایز"""
    width = get_terminal_width()
    welcome_text = "⚡ WELCOME TO FAROOQ TOOL ⚡"
    
    padding = (width - len(welcome_text)) // 2
    if padding < 0:
        padding = 0
    
    spaces = " " * padding
    
    print(f"\n{spaces}\033[1;33m{BOLD}{'=' * len(welcome_text)}{RESET}")
    print(f"{spaces}\033[1;32m{BOLD}{welcome_text}{RESET}")
    print(f"{spaces}\033[1;33m{BOLD}{'=' * len(welcome_text)}{RESET}\n")
    time.sleep(1)

def main():
    clear()
    welcome()
    time.sleep(0.5)
    clear()
    
    banner()
    
    print()
    print_centered_big("WELCOME TO FAROOOQ TOOLS")
    print()
    print()
    
    print_box1()
    print()
    print_box2()
    print()
    
    width = get_terminal_width()
    print(f"{GOLD_LINE}{BOLD}{'=' * min(width - 4, 60)}{RESET}")
    show_prompt()
    print()

if __name__ == "__main__":
    main() 
