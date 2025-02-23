import os
from colorama import init, Fore

init(autoreset=True)

host = input(Fore.MAGENTA + "Enter IP/Website: ")
count = input(Fore.MAGENTA + "Amount of times too ping : ")
size = input(Fore.MAGENTA + "Size of the packets!: ")

if not count.isdigit():
    print(Fore.MAGENTA + "Invalid number, using 4")
    count = "4"

if not size.isdigit():
    print(Fore.MAGENTA + "Invalid size, using 32")
    size = "32"

cmd = f"ping -n {count} -l {size} {host}"
resp = os.system(cmd)

if resp == 0:
    print(Fore.GREEN + f"{host} is online (yipee) ")
else:
    print(Fore.RED + f"{host} offline or wrong URL")
