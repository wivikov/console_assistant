import json

def load_users():
    try:
        with open("users.json", "r") as f:
            users =  json.load(f)
            return  users
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_user(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)


def register_user():
    users = load_users()
    username = input("Enter new username: ").lower()
    if username in users:
        print("Users already exist")
    else:
        password = input("Enter new password: ")
        users[username] = password
        save_user(users)
        print("User registered successfully!")

def login_user():
    users = load_users()
    login = input("Enter login:")
    password = input("Enter a password:")
    if login in users:
        if users[login] == password:
            print(f"Welcome , {login}")
        else:
            print("Wrong password")
    else:
        print("User not found")

