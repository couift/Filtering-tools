import random
import sys
from subprocess import call
from sys import platform
import time


red='\033[31m'
green='\033[32m'
blue='\033[36m'
pink='\033[35m'
boldblue='\033[0m'
#req


govxzarsh = ['This-channel-promotes-suicide','This-channel-promotes-violent-scenes','This-channel-promotes-self-abuse-and-other-abuse','This-channel-is-spamming','This-channel-promotes-hacking','This-channel-is-scamming','This-channel-posts-inappropriate-ads','This-channel-posts-videos-about-womens-dance','This channel is insulting','This channel-is-obscene','This-channel-promotes-breaking-norms','This-channel-promotes-nudity','This-channel-is-about-sexual-relations','This-channel-promotes-erotic-scenes','This-channel-insults-Islamic-affairs','This-channel-insults-the-IRGC','This-channel-curses-the-mobilization-of-the-oppressed','This-channel-is-an-anti-Islamic-revolution','This-channel-curses-Imam-Khomeini-and-Khamenei','This-channel-has-an-inappropriate-profile']

print(f"\033[35m")
print(f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣠⣤⣠⣄⣤⣠⣤⣠⣤⣠⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⡿⢛⠭⠿⣛⣛⣭⣭⣭⣟⣋⣩⣉⠉⠉⠉⠉⠉⠉⠉⠉⢈⣭⡭⠭⣥⠭⢥⣥⣉⣈⠭⠙⣿⣿⣶⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⢫⡮⣔⠡⠚⢛⣋⣩⣭⣍⣙⡛⢻⠿⣖⡬⣭⠿⠷⣶⣷⣿⣿⣵⢴⣟⡿⢿⣿⣶⣠⡩⣗⠨⡁⢌⠙⡿⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡱⣷⢾⣖⣴⣭⣷⣿⣿⣿⣷⣿⣿⣿⣯⣛⢿⣯⣷⣫⣭⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣮⡌⣿⡆⣳⣿⣿⣿⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⢏⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⣧⣜⣿⡿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣾⣿⣛⣿⢮⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣼⣧⣿⣿⣧⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣿⣿⣾⣯⢡⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣧⠀⠀⠀
⠀⠀⣠⣾⣿⢟⡭⢊⣝⣹⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣭⢿⡿⣿⣇⠀⠀
⠀⣰⣿⣽⠗⣽⣲⣿⣖⣬⣉⣉⡹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⢁⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠓⡋⢉⣉⣉⡁⠊⠻⡻⣮⢻⡆⠀
⢠⣿⣿⡏⣼⡿⣟⣽⣿⣿⣿⣶⣿⣦⣙⠯⣿⣿⠿⢿⣿⣿⣿⣿⢁⣀⠸⠀⠀⠀⠀⠀⢛⠋⢀⣈⢻⡿⣿⣟⣛⡿⠟⢁⣠⣶⣯⣷⣿⣿⣿⣿⣷⣄⠙⡝⡞⣿⠀
⢸⣿⢻⢸⣿⣴⣿⣿⣿⣿⣿⣿⣿⢿⣿⣷⣦⣜⣯⣛⣹⣞⣿⣙⡦⢿⣷⣄⡀⠀⠀⠀⠘⣾⣿⠟⣘⣭⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣧⠘⣾⣽⡆
⢸⣿⣬⢾⡿⣻⢻⣿⣿⣿⣿⣷⣤⣽⣉⠟⡟⡙⠟⣿⢿⣿⣿⣿⣿⣿⣿⣷⣮⣀⣒⣢⣾⣿⣿⣿⣿⡿⣿⠛⠙⡟⡟⢹⣹⣠⣿⣷⣾⣿⣿⡇⣿⣿⢻⡄⢉⣿⡇
⠀⢿⣿⡘⣷⣿⣸⣷⣿⣷⣿⣿⣿⢤⣭⣖⢧⣇⢰⠁⠈⡝⠐⠸⣿⡿⠋⠹⠘⢻⣿⠯⠁⠈⠻⡏⠁⠀⠁⡆⠀⡇⢰⣴⣟⡗⢯⣿⣿⣿⣿⡇⣿⡟⣾⡇⢸⣼⡇
⠀⠈⢿⣷⠈⢿⡏⣿⣿⣿⣿⣿⣾⣘⡫⡏⡟⣿⣿⣦⣰⡅⠀⠀⡇⠀⠀⠀⠀⠀⡃⠀⠀⠀⠀⡅⠀⠀⠀⡇⣀⣼⡿⣿⣮⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⢃⣶⡿⠀
⠀⠀⠈⠻⣷⣌⣾⢾⢿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣡⡋⠟⣷⣤⣴⣧⣤⣤⣤⣤⣴⣧⣦⣶⣶⣶⡿⣾⣿⣿⢿⣿⣾⣿⣾⡿⣿⣿⣽⣿⣿⣿⢹⣿⣿⠏⡝⢨⠇⠀
⠀⠀⠀⠀⠈⣿⣿⣿⣹⢿⣿⣿⣿⣿⣏⡱⣿⣿⣿⣿⣿⣏⣿⣸⣿⣹⣸⣹⣿⣸⣿⣏⣹⣷⡿⣇⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣿⡿⠁⣸⢀⡏⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣿⣿⣗⢬⡛⢿⢿⣿⣿⣿⣿⣿⣾⣏⡿⣿⣿⣾⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣟⣿⣿⣿⢿⣽⣿⣿⣿⣥⡾⢋⣥⣾⣷⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⡛⠯⣷⣭⡻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣽⠿⣿⣿⣿⡿⣿⣿⡿⣿⣿⡿⣟⢯⣏⣶⢿⢿⢏⣿⣿⣿⡿⡿⣻⣿⣷⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡦⡌⢷⣝⣯⣷⡝⢿⡿⣿⣾⣿⢿⣿⣿⣾⣹⣣⢏⣽⠹⣹⣘⣹⢠⣿⣾⣿⢃⣮⣾⣿⠟⠛⡩⢎⣼⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣮⣊⠻⣷⣽⣳⡈⢿⣯⢻⠿⢿⠿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⠿⢿⠿⠟⡿⡟⣳⢃⡴⠋⣠⢾⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣦⡙⢳⣿⢧⠈⢿⣿⣄⢸⡄⢸⡄⠀⠀⠀⠞⠀⠀⠀⢸⠀⢸⠀⣤⣣⡵⠣⠀⣠⡞⢡⣾⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣎⢳⡜⢿⣧⠈⢿⣿⣾⣧⢸⡇⠀⠀⢠⣯⣄⠀⠀⣸⢀⣾⣴⣿⡟⣡⢁⣾⠏⣴⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⡆⠰⠀⡹⡆⠈⢿⣿⣿⣾⣿⣇⣰⣿⣿⣾⣶⣷⣿⣿⣿⣿⡟⣰⢃⡼⠃⣾⣽⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣄⠑⡘⣷⣄⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢠⣯⠟⢁⣼⢿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣇⠀⠈⣿⢷⣀⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⡵⣫⡿⢀⣾⢯⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣦⡄⠐⠷⡙⢦⣀⠀⠈⠉⠉⠀⠀⣀⣀⣀⡤⠚⢱⡿⠁⣾⢣⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠀⠬⣭⣭⣉⣭⣭⣤⣤⣴⣥⡤⠊⠉⠀⡾⣡⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⠀⠒⠿⠿⢿⣿⣿⠿⠿⠟⠋⠀⠀⠀⣸⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⣀⣀⠀⠀⠀⠀⠀⢀⣀⣴⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

█▀▀ █▀█ █▀▄ █▀▀   █▀▄▀█ ▄▀█ █▄▀ █▀▀ █▀█   █▀▀ █ █░░ ▀█▀ █▀▀ █▀█ █   █▀▀ █ ▀█▀ ▄▀█ ▄▀█
█▄▄ █▄█ █▄▀ ██▄   █░▀░█ █▀█ █░█ ██▄ █▀▄   █▀░ █ █▄▄ ░█░ ██▄ █▀▄ █   ██▄ █ ░█░ █▀█ █▀█ v1.0⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
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
print('supports eitaa 6.4.14.0 version!   just fo')
print(f"\033[31m")
time.time()
print(" servers...............ON         just for channel.")
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


idta4get = input('id target channel ro bedoon @ vared con >>> ')

print(f"\033[36m")
print( random.choice(gvoxzarsh)+''+'https://eitaa.com/'+''+idta4get)
print(f"\033[36m")

time.sleep(5)
print(f"\033[32m")
print(' 30 sayer 40 mostahjan ')
  
time.sleep(10.6)
