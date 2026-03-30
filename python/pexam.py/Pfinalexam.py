
print()
print("Welcome to Inventory List Analyzer!")
print()

items = []

while True:
    item_name = input("Enter item name: ")
    category = input("Enter category: ")
    quantity = int(input("Enter quantity: "))

    items.append({
        "name": item_name,
        "category": category,
        "quantity": quantity
    })

    print()
    add_item = input("Do you want to add more items? (y/n): ")
    
    print()

    if add_item.lower() != "y":
        break

print()
print("=========== INVENTORY SUMMARY ===========")
print()

total_items = len(items)
print(f"Total Different Items: {total_items}")
names = [item['name'] 
        for item in items]
print(f"You entered {total_items} different items: {', '.join(names)}")
print()

total_quantity = sum(item['quantity'] for item in items)
print(f"Total Quantity in Stock: {total_quantity}")
print(f"Sum of all quantities: {total_quantity}")
print()

average_qty = total_quantity / total_items
print(f"Average Quantity per Item: {average_qty}")
print(f"Average = {total_quantity} total / {total_items} items")
print()

highest_item = max(items)
print(f"Most Stocked Item: {highest_item['name']} ({highest_item['quantity']} units)")
print(f"Explanation: {highest_item['name']} has the highest quantity.")
print()

lowest_item = min(items)
print(f"Least Stocked Item: {lowest_item['name']} ({lowest_item['quantity']} units)")
print(f"Explanation: {lowest_item['name']} has the lowest quantity.")
print()

categories = (category)
print(f'Unique Categories in Inventory: {[categories]}')
print(f"Explanation: categories are taken from user input and converted to lowercase.")
print("No duplicates are shown here.")

print()
print("-------------------------------------------------------")

print("📦 Items Sorted by Quantity (High to Low):- ")
print()

sorted_items = sorted(items)

for i, item in enumerate(sorted_items, start=1):
    print(f"{i}. {item['name']} - {item['quantity']} units")

print()
print("Explanation: Items are sorted using the quantity from highest to lowest.")
print()

print("---------------------------------------------")
print()

print("📁 Categories in Alphabetical Order:- ")
print()

ct_n = sorted(category)
print(f"Category:- ", ct_n)

print()
print("Explanation: The set of unique categories was sorted alphabetically for display. ")
print()

print("=========== END OF REPORT ==========")
print()
