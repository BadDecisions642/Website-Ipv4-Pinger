import subprocess
from colorama import init, Fore

init(autoreset=True)

def get_input(prompt):
    return input(Fore.MAGENTA + prompt + Fore.RESET).strip()

host = get_input("Enter a IPv4/Website-URL to ping: ")
while not host:
    print(Fore.RED + "You must input something!")
    host = get_input("Enter a IPv4/Website-URL to ping: ")

count = get_input("Enter the number of times to ping: ")
while not count.isdigit():
    print(Fore.RED + "That's not a valid number!")
    count = get_input("Enter the number of times to ping: ")

ping_command = ["ping", "-n" if count else "-c", str(count), host]
print(Fore.MAGENTA + f"\nPinging {host} {count} times...")

try:
    result = subprocess.run(ping_command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode == 0:
        print(Fore.MAGENTA + f"\n{host} is valid.")
        for line in result.stdout.splitlines():
            if "time=" in line:
                ping_time = line.split("time=")[1]
                print(Fore.YELLOW + f"Ping: {ping_time.strip()}")
    else:
        print(Fore.RED + f"\n{host} is offline or invalid.")
except FileNotFoundError:
    print(Fore.RED + "\nPing command not found on your system.")
except Exception as e:
    print(Fore.RED + f"\nError: {e}")