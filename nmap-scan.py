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

ip_nmap = input("IP Target : ")
nmap_comand = "nmap -sS -p0-65535 " + ip_nmap
os.system(nmap_comand)
