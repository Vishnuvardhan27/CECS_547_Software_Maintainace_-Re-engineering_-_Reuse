#Code Smells Example for long method
def calculate_item_price(item):
    if item.quantity > 0:
        if item.price > 100:
            return item.price * 0.9
        else:
            return item.price * 0.95
    else:
        return 0

def calculate_total_price(items):
    total = 0
    for item in items:
        total += calculate_item_price(item)
    return total


# In this refactored code:

# 1. `calculate_item_price(item)` is a new function that calculates the price for an individual item based on the quantity and price conditions. This function makes the code more readable and easier to understand.

# 2. `calculate_total_price(items)` still calculates the total price, but it now delegates the item price calculation to the `calculate_item_price` function.

# Breaking down the code into smaller functions not only reduces the method's length but also makes it more modular and easier to maintain.
