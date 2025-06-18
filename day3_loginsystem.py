users_db = {
    "admin": "qwerty",
    "guest": "1234",
    "bodik": "python"
}

def login_system(username, password):
    username = username.lower()
    if username in users_db:
        if users_db[username] == password:
            return f"Welcome {username}!"
        else:
            return "Wrong password"
    else:
        return "No such user"
def register_user():
    username = input("Enter new user name:")
    if username in users_db:
        print("User already exist!")
    else:
        password = input("Enet new password!")
        users_db[username] = password
        print(f"User {username} register successfully!")
if __name__ == "__main__":
    register_user()
    print(users_db)
