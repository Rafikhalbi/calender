import calendar
import os
os.system('clear')
#input

banner="""
________ _______ __________________
___  __ \___    |___  ____/____  _/ \t-={ creat by : Rafi }=-
__  /_/ /__  /| |__  /_     __  /\t _____rafi tools_____
_  _, _/ _  ___ |_  __/    __/ /   
/_/ |_|  /_/  |_|/_/       /___/   \t\x1b[1;96mcalender sederhana\n\t\t\t\t\tdengan python \x1b[1;91m2.7\x1b[1;97m

[ \x1b[1;92mmencari tanggal dengan python !\x1b[1;97m ]
______________________________________________________________"""
print(banner)
print
tahun = int(input("Tahun : \x1b[1;96m"))
bulan = int(input("\x1b[1;97mBulan : \x1b[1;96m"))
# out put
print '\x1b[1;93m'
print(calendar.month(tahun, bulan))
print '\x1b[1;97m'