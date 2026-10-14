# Dictionary of items and their prices
Prices = {
    "apple": 20,
    "banana": 10,
    "milk": 30,
    "bread": 25,
    "eggs": 50
}

# Items that are out of stock
out_of_stock = {"banana", "eggs"}

# List of ordered items
Order = ["apple", "banana", "milk", "bread", "eggs"]

# Initial total
total = 0

# Loop through each item in the order
for item in Order:
    if item in out_of_stock:
        print(item, "is unavailable")
    else:
        total += Prices[item]

# Print final order value
print("Final order value:", total)