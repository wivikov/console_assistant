def process_shopping_list(input_string):
    if not input_string.strip():
        return "Nothing to buy"

    items_raw = input_string.split(',')
    clean_items = [item.strip().lower() for item in items_raw]

    item_counts = {}
    for item in clean_items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

    result = {
        "unique_items": list(item_counts.keys()),
        "total": sum(item_counts.values()),
        "counts": item_counts
    }
    return result

shopping = process_shopping_list("apple, banana, apple, Cherry, apple, banana")

print("Список унікальних товарів:", shopping["unique_items"])
print("Загальна кількість товарів:", shopping["total"])
print("Кількість кожного товару:")
for item, count in shopping["counts"].items():
    print(f"– {item}: {count}")
