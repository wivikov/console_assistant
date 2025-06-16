users = {
    "admin": "1234",
    "user1": "qwerty",
    "user2": "letmein"
}
login = input("Enter you login")
password = input("Enter you password:")
if login in users:
    if users[login] == password:
        print(f"welcome, {login}!")
    else:
        print("Error password.")
else:
    print("User not found")

orders = ["apple", "banana", "apple", "banana", "apple", "cherry", "cherry"]
orders_list = {}

for item in orders :
    if item in orders_list:
        orders_list[item] += 1
    else:
        orders_list[item] = 1
print(orders_list)

settings = ("datk_mode", "Language", "timezone")
values = ("on", "en", "UTC+2")

config = dict(zip(settings, values))

print(config)
