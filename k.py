import random

# List of available ingredients
ingredients = ["Vanilla", "Chocolate", "Strawberry", "Mint"]

# Dictionary to store customer orders
orders = {}

# Function to take customer orders
def take_order():
    customer_name = input("Enter customer name: ")
    order = random.choice(ingredients)
    orders[customer_name] = order

# Function to prepare ice cream
def prepare_ice_cream():
    customer_name = input("Enter customer name: ")
    if customer_name in orders:
        order = orders[customer_name]
        print("Preparing ice cream with", order, "flavor...")
        # Add more logic here for preparing the ice cream
        print("Ice cream prepared!")
        orders.pop(customer_name)
    else:
        print("Invalid customer name.")

# Main game loop
while True:
    print("1. Take Order")
    print("2. Prepare Ice Cream")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        take_order()
    elif choice == "2":
        prepare_ice_cream()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

print("Game over!")
