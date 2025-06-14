scores = {
    "Anna": 90,
    "Oleh": 78,
    "Ivan": 82,
    "Maria": 95
}

print("Student with score more than 80:")
for student, score in scores.items():
    if score > 80:
        print(f"{student}: {score}")

average_score = sum(scores.values()) / len(scores)
print(f"\nAvarage score: {average_score:.2f}")

products = ["apple", "banana", "apple", "orange", "banana", "cherry"]
my_products = set(products)

print(my_products)

data = ("dark_mode", "language_en", "timezone_utc+2")
print(data[0])
print(data[1])
print(data[2])

