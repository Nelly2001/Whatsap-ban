import os
import time
import requests
from termcolor import colored

def print_loading_bar():
    for i in range(101):
        print(f"\r{colored('Banning in progress...', 'red')} [{'=' * (i // 10)}{' ' * (10 - i // 10)}] {i}%", end='')
        time.sleep(0.1)
    print()

def send_spam_report(number):
    url = "https://example.com/spam_report"  # Replace with the actual WhatsApp spam report URL
    data = {
        "number": number,
        "reports": 500
    }
    response = requests.post(url, data=data)
    return response.status_code == 200

def main():
    print(colored("  ███╗   ██╗███████╗██╗     ██╗  ██╗   ██╗               ║
║              ████╗  ██║██╔════╝██║     ██║  ╚██╗ ██╔╝               ║
║              ██╔██╗ ██║█████╗  ██║     ██║   ╚████╔╝                ║
║              ██║╚██╗██║██╔══╝  ██║     ██║    ╚██╔╝                 ║
║              ██║ ╚████║███████╗███████╗███████╗██║                  ║
║              ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝╚═╝",
this tool is made by bhadboy NELLY'red'))
    while True:
        print("1. Ban Permanent")
        print("2. Ban Temporary")
        choice = input("Select an option: ")

        if choice == '1':
            number = input("Input the fucker number (e.g., 2349058727403): ")
            if not number.isdigit() or len(number) != 11:
                print("Invalid number. Please check the number.")
                continue
            print_loading_bar()
            if send_spam_report(number):
                print("Done. Press 'x' to go back.")
            else:
                print("Failed to ban the number. Press 'x' to go back.")
        elif choice == '2':
            number = input("Input the fucker number (e.g., 2349058727403): ")
            if not number.isdigit() or len(number) != 11:
                print("Invalid number. Please check the number.")
                continue
            print_loading_bar()
            if send_spam_report(number):
                print("Done. Press 'x' to go back.")
            else:
                print("Failed to ban the number. Press 'x' to go back.")
        elif choice == 'x':
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
