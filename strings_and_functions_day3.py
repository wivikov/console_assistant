name = input("Enter your name:")
name = name.capitalize()
print(f"Hello, {name}")

text = "Python is awesome and Python is fun"
text = text.replace("Python","Django")
print(text)


def check_password(password):
    if len(password) <8:
        print("password is incorect")
    elif "123" in password:
        print("password is  too  weak")
    else:
        print("Password accept")

user_input = input('Eneter your password')
check_password(user_input)

minitext = input("Enter text: ")
reversed_text = minitext[::-1]
print("Reversed:" , reversed_text)
