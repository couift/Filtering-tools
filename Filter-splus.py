import random
import sys
from subprocess import call
from sys import platform
import time
import datetime


red='\033[31m'
green='\033[32m'
blue='\033[36m'
pink='\033[35m'
boldblue='\033[0m'
#requments


goxzarsh = ['This-account-mocks-Islamic-affairs','This-account-promotes-pornography','Hello-this-person-has-an-inappropriate-profile','This-account-promotes-nakedness-and-veiling','This-account-is-a-spammer','This account-is-not-good-for-Soroush Plus-messenger-because-it-is-a-real-bully']

print(f"\033[35m")
x = f"""
⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣟⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣾⣯⣽⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣽⣿⣦⣀⠀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣟⣻⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣟⣭⣿⣷⣄⠀⠀⠀
⠀⢠⣾⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣫⣿⣷⡀⠀
⢠⣿⣿⣟⣛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡄
⣺⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⡷
⢹⣿⣿⡿⣿⣻⣆⠀⠀⠀⠀⠀⢻⡷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢎⣿⠀⠀⠀⠀⠀⢀⣠⠾⣿⣿⣿⣿⣿⣿⠇
⠈⠻⣿⣷⣿⣿⣿⠿⣦⣤⣀⠀⢠⣷⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢺⣿⣦⣀⣠⣴⣾⡿⣿⣿⣷⣶⣶⣶⡿⠋⠀
⠀⠀⠙⠿⣿⣟⣵⣿⣿⣿⢿⣷⣼⣧⣿⣧⣠⣤⣤⣤⣤⣤⣤⡤⣤⢤⣾⣯⣿⣿⣿⣿⣭⣽⣿⣶⣿⣿⡿⠟⠋⠀⠀⠀
⠀⠀⠀⠀⠈⠛⢿⣯⣵⠶⠟⢛⣋⠭⢭⡐⠖⠤⠥⠔⠲⠰⠊⠥⠭⠨⣅⣀⣅⡚⢭⡙⠻⢿⣷⣿⣟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣾⠟⢫⣼⠵⠊⠅⡡⠄⡂⠀⠀⡐⢒⠢⡔⠢⢒⠤⣢⢖⠲⠦⣜⢍⠓⢌⠳⡐⢌⣍⣻⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⡧⣼⠷⣵⣆⠴⡃⠀⠀⢡⢓⠠⠄⣩⡞⣍⣣⠀⣼⠣⠈⠁⠱⣈⢷⡀⠂⠐⢀⠒⣫⢙⢻⣧⡀⠀⠀⠀⠀
⠀⠀⣀⣴⣿⣶⣷⣼⣡⠌⡳⣕⢢⠐⢦⠋⠠⣞⠁⠸⡯⢈⠸⣇⠧⣀⠀⢤⡘⢦⡷⣼⠻⠩⠶⢶⣭⣤⠹⣷⣦⡀⠀⠀
⠀⢸⡟⣩⣿⠳⣿⣦⣝⡩⣆⠐⠂⢘⣰⡶⢶⡏⠄⡐⠀⠲⠦⣬⣓⠣⠏⠖⣩⠏⢀⠈⣰⣶⣿⣿⢻⣿⡻⣜⣿⢿⣄⠀
⠀⢸⡿⣧⢻⣄⣿⣿⣿⣿⣿⣯⣕⣚⡁⣾⡋⣠⢐⠿⠷⣶⡀⣷⠈⠓⢄⣂⣴⣚⣤⣾⣿⣿⣿⢣⡟⣼⡗⣿⣺⣗⢻⡆
⠀⢿⣧⡷⣆⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⡟⣁⡟⡆⠠⣏⣧⣸⡧⣼⡇
⠀⠀⢻⣧⡟⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣄⢻⡽⣛⡽⡛⣏⢌⣿⠟⠁
⠀⠀⠀⢻⣿⢸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⡼⡁⣞⢐⡎⠓⣞⣿⠿⠁⠀⠀
⠀⠀⠀⢸⣿⣺⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⢟⣵⣃⣿⡉⣆⡧⢌⣿⠇⠀⠀⠀⠀
⠀⠀⠀⢸⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣻⡟⢱⡼⠋⣋⡯⢵⡟⣑⣼⠟⠀⠀⠀⠀⠀
⠀⠀⠀⢿⣧⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣫⡿⢁⡼⢫⡜⣱⠏⣠⣏⣶⡿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⢿⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣋⣽⠟⣠⡯⡿⢏⡼⣣⣾⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⣿⢿⣧⡻⢽⡿⡿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣟⢻⢿⣿⡿⠛⡝⣩⣾⣿⡾⣿⠟⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⣶⣏⡟⣧⣉⠿⢛⠿⠯⣬⡿⠦⠷⠚⣖⢿⢷⢞⢋⣴⣷⣿⠿⠛⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠿⣿⣟⣿⣯⠽⢯⠵⣤⣕⣭⣤⣾⠿⢿⠿⠟⠛⠋⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠉⠋⠛⠛⠛⠋⠋⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
█▀▀ █▀█ █▀▄ █▀▀   █▀▄▀█ ▄▀█ █▄▀ █▀▀   █▀▀ █ █░░ ▀█▀ █▀▀ █▀█ █   █▀ █▀█ █░░ █░█ █▀
█▄▄ █▄█ █▄▀ ██▄   █░▀░█ █▀█ █░█ ██▄   █▀░ █ █▄▄ ░█░ ██▄ █▀▄ █   ▄█ █▀▀ █▄▄ █▄█ ▄█ v1.0 
"""
for c in x:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.0000001)
#i'm god man

time.sleep(1)


time.sleep(0.1)
print(f"\033[31m")
print(" programing by DMNHACKER ")
print(f"\033[31m")
print('supports soroush plus 6.5.0.0 version!')
print(f"\033[31m")
time.time()
print(" servers.....ON at          ")
print(f"{blue} ")
time.sleep(2.5)
print ("")
time.sleep(0.7)
print (".........")
time.sleep(0.6)
print ("........")
time.sleep(0.5)
print (".......")
time.sleep(0.4)
print ("......")
time.sleep(0.3)
print (".....")
time.sleep(0.2)
print ("....")
time.sleep(0.1)
print ("...")
time.sleep(0.5)
print ("..")
time.sleep(0.1)
print (".")
time.sleep(0.5)
print(f"\033[31m")
print ("installed!")
time.sleep(3)
print ("")


'idta3get' == input('id target ro bedoon @ vared con >>> ')

print(f"\033[36m")
print(random.choice(goxzarsh)+""https://splus.ir""+'idta3get')
print(f"\033[36m")

time.sleep(5)
print(f"\033[32m")
print(' 30 sayer 40 mostahjan ')
  
time.sleep(10.6)
