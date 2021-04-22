import os
import time

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

modalita = 'dos' , 'nmap scan'

os.system("clear")
print (logo)
print (" ")
print ("Github   : https://github.com/windows-d")
print ("Telegram : @micheleakabstees")
print (" ")

print(modalita)
mod = input("Scegli che funzione usare: ")

if mod == "dos":
    os.system("python3 dos.py")

if mod == "nmap scan":
    os.system("python3 nmap-scan.py")
