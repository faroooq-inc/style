#!/usr/bin/env python3
import os

logo = '''
╔════════════════════════════════════╗
║        FAROOQ HACK TOOL           ║
║        MIX COLOR EDITION          ║
╚════════════════════════════════════╝

[01] Quick Start - on/off
[02] Servers Setting
[03] Extra Keys
[04] Add to Startup
[05] System Process Viewer
[06] Exit Tool
'''

def banner():
    # send logo to lolcat for rainbow effect
    os.system("echo '{}' | lolcat -p 1.6".format(logo))

if __name__ == "__main__":
    banner()
