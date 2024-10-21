import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start():
    while True:
        clear_screen()  # Clear the screen before stuff :(
        print("Pick an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        op = input("Select an option (1-5): ")

        if op == '5':
            print("Exiting...")
            break  # Exit the loop

        # Get numbers
        x = float(input("Number one? "))
        y = float(input("Number two? "))

        if op == '1':
            print("The answer is:", x + y)

        elif op == '2':
            print("The answer is:", x - y)
# if you can see this send help im in desperate need of melatonin 😊
        elif op == '3':
            print("The answer is:", x * y)

        elif op == '4':
            if y != 0:
                print("The answer is:", x / y)
            else:
                print("Error: Division by zero is not allowed.")

        else:
            print("Invalid option, please try again.")

        input("Press Enter to continue...")  #user input before clearing the screen

if __name__ == "__main__":
    start()
