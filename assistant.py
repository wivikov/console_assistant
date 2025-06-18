from day5_task import calculator
from day3_loginsystem import login_system
from day3_loginsystem import register_user
from day4_1block import process_shopping_list
from file_login_system import register_user, login_user

def main_menu():
    while True:
        print("\n==== assistant ====")
        print("1 Calculator:")
        print("2 Shopping List")
        print("3 Login-system")
        print("4 Exit")

        choice = input("Enter option (1-4)")
        if choice == "1":
            a = input("Enter first number:")
            b = input("Enter second number:")
            operation = input("choose operation (+ - * /): ")
            result = calculator(a, b, operation)
            print("Result:", result)
        elif choice == "2":
            print("\n-- Shopping list --")
            user_input = input("Enter items separeted by commas:")
            process_shopping_list(user_input)
        elif choice == "3":
            print("\n-- Login System --")
            action = input("Type 'login' or 'register'").lower()
            if action == "login":
                login_user()
            elif action == "register":
                register_user()
            else:
                print("Unknown action.")
        elif choice == "4":
            print("Thanks Bye")
            break
        else:
            print("Incorrect choice. Try again.")

main_menu()