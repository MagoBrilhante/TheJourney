##################################- IMPORTS -##################################
from time import sleep
import os

##################################- VARIABLES -##################################
yes = ['Y', 'YES', '1']
no = ['N', 'NO', '0']

##################################- MAIN -##################################
def main():
    clear_screen()
    while True:
        try:
            user_timer = int(input("Timer: "))
            if user_timer > 0:
                timer(user_timer)
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("ValueError: Invalid input. Please enter an integer.")

##################################- TIMER -##################################
def timer(seconds):
    while seconds != 0:
        clear_screen()
        print(seconds)
        sleep(1)
        seconds = seconds - 1
    clear_screen()
    print('0\n =-=-=-=- END -=-=-=-=')
    sleep(1)
    clear_screen()
    choose()

##################################- CHOOSE -##################################
def choose():
    while True:
        choice = input('Do you want to continue?(Y/N) ').upper().strip()
        if choice in yes:
            main()
        elif choice in no:
            clear_screen()
            print('=-=-=-=- GOODBYE -=-=-=-=')
            break
        else:
            clear_screen()
            print("Send a valid input: Y, N, 1, 0.")

##################################- CLEAR SCREEN -##################################
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

##################################- RUN -##################################
if __name__ == '__main__':
    main()
