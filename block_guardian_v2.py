#!/usr/bin/env python3
import random
import string
from colorama import Fore, Style, init
init(autoreset=True)

def banner():
    print(Fore.GREEN + """
██████╗ ██╗      ██████╗  ██████╗██╗  ██╗
██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝
██████╔╝██║     ██║   ██║██║     █████╔╝ 
██╔══██╗██║     ██║   ██║██║     ██╔═██╗ 
██████║ ███████╗╚██████╔╝╚██████╗██║  ██╗
╚═╝  ╚═╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
    GUARDIAN v2.0
    """ + Style.RESET_ALL)
    print(Fore.CYAN + "[+] Developed by: H BOY")
    print(Fore.CYAN + "[+] Motto: FROM THE BLOCK TO THE WORLD")
    print(Fore.CYAN + "[+] Status: UNLOCKED")
    print(Fore.CYAN + "[+] Features: TESTER + GENERATOR\n")

def test_password(pwd):
    score = 0
    if len(pwd) >= 8: score += 1
    if any(c.islower() for c in pwd): score += 1
    if any(c.isupper() for c in pwd): score += 1
    if any(c.isdigit() for c in pwd): score += 1
    if any(c in "!@#$%^&*()_+" for c in pwd): score += 1
    
    if score <= 2:
        return Fore.RED + "WEAK ❌ - Hackers can break this in minutes"
    elif score == 3 or score == 4:
        return Fore.YELLOW + "MEDIUM ⚠️ - Can be cracked"
    else:
        return Fore.GREEN + "STRONG ✅ - Unbreakable"

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    pwd = ''.join(random.choice(chars) for _ in range(16))
    return pwd

if __name__ == "__main__":
    banner()
    while True:
        print(Fore.WHITE + "[ MENU ]")
        print("1. Test Your Password")
        print("2. Generate Strong Password")
        print("3. Exit")
        choice = input(Fore.WHITE + "\n[H BOY] Select option: ")
        
        if choice == '1':
            pwd = input("Enter password to test: ")
            print(test_password(pwd))
        elif choice == '2':
            new_pwd = generate_password()
            print(Fore.GREEN + f"New Strong Password: {new_pwd}")
            print(Fore.YELLOW + "Save this password now!")
        elif choice == '3':
            break
        else:
            print(Fore.RED + "Invalid choice")
        print("")

