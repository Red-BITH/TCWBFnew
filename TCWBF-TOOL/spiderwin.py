import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import time
import os
import json
import getmac

class IPQuery:
    def __init__(self, ip):
        self.ip = ip
        self.ipapi_url = f"https://ipapi.co/{ip}/json/"
        self.ipinfo_url = f"https://ipinfo.io/{ip}/json"

    def make_request(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            return None
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
            return None
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
            return None
        except requests.exceptions.RequestException as err:
            print(f"Oops, Something went wrong... {err}")
            return None

    def get_ipapi_info(self):
        ipapi_data = self.make_request(self.ipapi_url)
        return ipapi_data

    def get_ipinfo_info(self):
        ipinfo_data = self.make_request(self.ipinfo_url)
        return ipinfo_data

    def get_mac_address(self):
        mac_address = getmac.get_mac_address(ip=self.ip)
        return mac_address

    def perform_query(self):
        ipapi_info = self.get_ipapi_info()
        ipinfo_info = self.get_ipinfo_info()
        mac_address = self.get_mac_address()

        return {
            "ipapi_info": ipapi_info,
            "ipinfo_info": ipinfo_info,
            "mac_address": mac_address
        }

def whois_lookup(domain):
    # Domain için WHOIS sorgusu yapma
    url = f'https://www.whois.com/whois/{domain}'
    response = requests.get(url)
    
    # WHOIS verilerini çekme ve işleme
    soup = BeautifulSoup(response.text, 'html.parser')
    whois_data = soup.find('pre', class_='df-raw')
    
    if whois_data:
        print(Fore.GREEN + f"WHOIS Bilgileri {domain}:\n{whois_data.text}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"WHOIS Bilgileri {domain} bulunamadı." + Style.RESET_ALL)

def manual_ip_query():
    # Kullanıcıdan IP adresi girmesini iste
    ip = input("Lütfen bir IP adresi girin: ").strip()
    print(f"Manuel olarak sorgulanan IP adresi: {ip}\n")

    ip_query = IPQuery(ip)
    query_result = ip_query.perform_query()

    if query_result["ipapi_info"] and query_result["ipinfo_info"]:
        print("ipapi.co Bilgileri:")
        print(json.dumps(query_result["ipapi_info"], indent=2))

        print("\nipinfo.io Bilgileri:")
        print(json.dumps(query_result["ipinfo_info"], indent=2))

        print("\nMAC Adresi:")
        print(query_result["mac_address"])
    else:
        print("IP info request failed.")

def main():
    while True:
        print("\n1. WHOIS Sorgusu")
        print("2. IP Sorgusu (Manuel IP)")
        print("3. Çıkış")
        
        choice = input("Seçiminiz: ")
        
        if choice == '1':
            target_domain = input("Hedef domain: ").strip()
            whois_lookup(target_domain)
        elif choice == '2':
            manual_ip_query()
        elif choice == '3':
            print(Fore.YELLOW + "Programdan çıkılıyor." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Geçersiz seçenek. Lütfen tekrar deneyin." + Style.RESET_ALL)

if __name__ == "__main__":
    print("""\033[31m

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
    time.sleep(2)
    os.system("pip install requests")
    os.system("pip install beautifulsoup4")
    os.system("pip install colorama")
    os.system("pip install getmac")
    os.system("clear")
    main()
