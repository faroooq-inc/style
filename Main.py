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

# د بکس شالید لپاره رنګونه
# لومړی بکس (نسواري-طلایی)
BOX1_BG = "\033[48;2;139;69;19m"        # SaddleBrown
BOX1_BG_LIGHT = "\033[48;2;160;82;45m"  # Sienna

# دویم بکس (نیلي-شنه + طلایی ترکیب)
BOX2_BG = "\033[48;2;0;100;80m"         # Teal (نیلي-شنه)
BOX2_BG_LIGHT = "\033[48;2;0;128;128m"  # DarkCyan
BOX2_TEXT_HIGHLIGHT = "\033[38;2;255;215;0m"  # د متن لپاره طلایی

# د کرښو لپاره ځانګړي رنگین کوډونه
LINE_BOLD = "\033[1m"

# د پرامپټ درې مختلف رنګونه
RED_ARROW = "\033[91m"
GREEN_ARROW = "\033[92m"
BLUE_ARROW = "\033[94m"

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
    """لومړی بکس - نسواري/طلایی رنګونه - دوه چنده لوړ (زیات عمق)"""
    width = get_terminal_width()
    line_width = min(width - 4, 75)
    
    # پورتنۍ کرښه - د اصل کوډ په څیر هنري
    print(f"{LINE_BOLD}{DARK_GOLD}{'═' * 20}{GOLD_LINE}» ───── «◊•» ✠ • ◊ «─────» «{DARK_GOLD}{'═' * 20}{RESET}")
    
    # خالي کرښه (د عمق لپاره)
    print(f"{BOX1_BG}{WHITE_TEXT}{BOLD}║{' ' * (line_width - 2)}{RESET}{BOX1_BG}{BOLD}║{RESET}")
    
    # د معلوماتو کرښې
    info_lines = [
        f"  {GOLD_LINE}Developer   >>{WHITE_TEXT} Faroooq Inc",
        f"  {GOLD_LINE}Tool Type   >>{WHITE_TEXT} FILExRANDOM",
        f"  {GOLD_LINE}Github      >>{WHITE_TEXT} github.com/porn-404",
        f"  {GOLD_LINE}Version     >>{WHITE_TEXT} V2.7"
    ]
    
    for info in info_lines:
        info_len = len(info.replace(GOLD_LINE, '').replace(WHITE_TEXT, '').replace(RESET, ''))
        padding_needed = line_width - info_len - 4
        if padding_needed < 0:
            padding_needed = 0
        print(f"{BOX1_BG}{WHITE_TEXT}{BOLD}║{info}{' ' * padding_needed} {RESET}{BOX1_BG}{BOLD}║{RESET}")
    
    # بله خالي کرښه (د عمق لپاره)
    print(f"{BOX1_BG_LIGHT}{WHITE_TEXT}{BOLD}║{' ' * (line_width - 2)}{RESET}{BOX1_BG_LIGHT}{BOLD}║{RESET}")
    
    # د فرعي معلوماتو لپاره اضافي کرښه
    print(f"{BOX1_BG_LIGHT}{WHITE_TEXT}{BOLD}║  {GOLD_LINE}Status      >>{WHITE_TEXT} Active{' ' * (line_width - 28)}{RESET}{BOX1_BG_LIGHT}{BOLD}║{RESET}")
    
    # خالي کرښه
    print(f"{BOX1_BG}{WHITE_TEXT}{BOLD}║{' ' * (line_width - 2)}{RESET}{BOX1_BG}{BOLD}║{RESET}")
    
    # ښکته کرښه - د اصل کوډ په څیر
    print(f"{LINE_BOLD}{DARK_GOLD}╚{'═' * 20} ──•◆•── ────────────────•✦•───────────────────╝{RESET}")

def print_box2():
    """دویم بکس - نیلي-شنه (Teal) او طلایی رنګونه - دوه چنده لوړ (زیات عمق)"""
    width = get_terminal_width()
    line_width = min(width - 4, 75)
    
    # پورتنۍ کرښه
    print(f"{LINE_BOLD}{LIGHT_GOLD}{'═' * 20}{RED_GOLD}» ───── «◊•» ✠ • ◊ «─────» «{LIGHT_GOLD}{'═' * 21}{RESET}")
    
    # خالي کرښه
    print(f"{BOX2_BG}{BOX2_TEXT_HIGHLIGHT}{BOLD}║{' ' * (line_width - 2)}{RESET}{BOX2_BG}{BOLD}║{RESET}")
    
    # د معلوماتو کرښې
    info_lines = [
        f"  {WHITE_TEXT}Operator        >> {BOX2_TEXT_HIGHLIGHT}0171{WHITE_TEXT}",
        f"  {WHITE_TEXT}Total Account   >> {BOX2_TEXT_HIGHLIGHT}5000{WHITE_TEXT}",
        f"  {WHITE_TEXT}⚡ Use Airplane (Flight) Mode For Speed Up",
        f"  {WHITE_TEXT}[!] {BOX2_TEXT_HIGHLIGHT}Turn on Flight Mode for best results{WHITE_TEXT}"
    ]
    
    for info in info_lines:
        info_len = len(info.replace(BOX2_TEXT_HIGHLIGHT, '').replace(WHITE_TEXT, '').replace(RESET, ''))
        padding_needed = line_width - info_len - 4
        if padding_needed < 0:
            padding_needed = 0
        print(f"{BOX2_BG}{BOX2_TEXT_HIGHLIGHT}{BOLD}║{info}{' ' * padding_needed}{RESET}{BOX2_BG}{BOLD}║{RESET}")
    
    # اضافي معلوماتي کرښه
    print(f"{BOX2_BG_LIGHT}{BOX2_TEXT_HIGHLIGHT}{BOLD}║  {WHITE_TEXT}Speed         >> {BOX2_TEXT_HIGHLIGHT}MAXIMUM{WHITE_TEXT}{' ' * (line_width - 27)}{RESET}{BOX2_BG_LIGHT}{BOLD}║{RESET}")
    
    # خالي کرښه
    print(f"{BOX2_BG}{BOX2_TEXT_HIGHLIGHT}{BOLD}║{' ' * (line_width - 2)}{RESET}{BOX2_BG}{BOLD}║{RESET}")
    
    # ښکته کرښه
    print(f"{LINE_BOLD}{LIGHT_GOLD}╚{'═' * 20} ──•◆•── ────────────────•✦•───────────────────╝{RESET}")

def show_prompt():
    """ترمینل پرامپټ - درې مختلف رنګونه"""
    print(f"\n\033[93m{BOLD}┌─[h4ck3r@termux]-[~]\033[0m")
    # درې مختلف رنګونه: سور، شین، نیلي
    print(f"{BOLD}{RED_ARROW}└──╼ ❯{RESET}{BOLD}{GREEN_ARROW}❯{RESET}{BOLD}{BLUE_ARROW}❯{RESET} \033[0m", end="")

def welcome():
    """د ویلکم مسیج - لوی سایز"""
    width = get_terminal_width()
    welcome_text = "⚡ WELCOME TO FAROOQ TOOL ⚡ ⚡ WELCOME TO FAROOQ TOOL ⚡"
    
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
    
    # لوګو د lolcat سره
    banner()
    
    # ځانګړی متن - سنټر، دوه چنده لوی، نیم سور نیم زرغون
    print()
    print_centered_big("WELCOME TO FAROOOQ TOOLS")
    print()
    print()
    
    # بکسونه د نوي شکل سره - اوس دواړه عرض او عمق لري
    print_box1()
    print()
    print_box2()
    print()
    
    width = get_terminal_width()
    print(f"{GOLD_LINE}{BOLD}{'=' * min(width - 4, 60)}{RESET}")
    show_prompt()

if __name__ == "__main__":
    main() 
