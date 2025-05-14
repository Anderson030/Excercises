menu = []

def add_dish():
    name = input("Enter dish name: ").strip()
    try:
        price = float(input("Enter dish price: "))
        available = input("Is it available? (yes/no): ").strip().lower() == "yes"
        menu.append({"name": name, "price": price, "available": available})
        print("Dish added.\n")
    except ValueError:
        print("Invalid price.\n")

def change_availability():
    name = input("Enter dish name to change availability: ").strip()
    for dish in menu:
        if dish["name"].lower() == name.lower():
            dish["available"] = not dish["available"]
            print("Availability updated.\n")
            return
    print("Dish not found.\n")

def total_available_price():
    total = sum(d["price"] for d in menu if d["available"])
    print(f"Total price of available dishes: ${total:.2f}\n")

# Example menu
def menu_system():
    while True:
        print("1. Add Dish")
        print("2. Change Availability")
        print("3. Total Available Price")
        print("4. Exit")
        option = input("Choose an option: ").strip()
        if option == "1":
            add_dish()
        elif option == "2":
            change_availability()
        elif option == "3":
            total_available_price()
        elif option == "4":
            break
        else:
            print("Invalid option.\n")

menu_system()
