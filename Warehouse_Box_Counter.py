warehouse = {}

def add_box():
    name = input("Enter box name: ").strip()
    try:
        quantity = int(input("Enter quantity: "))
        warehouse[name] = quantity
        print("Box added.\n")
    except ValueError:
        print("Invalid quantity.\n")

def update_quantity():
    name = input("Enter box name to update: ").strip()
    if name in warehouse:
        try:
            quantity = int(input("Enter new quantity: "))
            warehouse[name] = quantity
            print("Quantity updated.\n")
        except ValueError:
            print("Invalid quantity.\n")
    else:
        print("Box not found.\n")

def has_enough():
    name = input("Enter box name: ").strip()
    try:
        required = int(input("Enter required amount: "))
        if warehouse.get(name, 0) >= required:
            print("Enough boxes available.\n")
        else:
            print("Not enough boxes.\n")
    except ValueError:
        print("Invalid number.\n")

# Example menu
def menu():
    while True:
        print("1. Add Box")
        print("2. Update Quantity")
        print("3. Check if Enough")
        print("4. Exit")
        option = input("Choose an option: ").strip()
        if option == "1":
            add_box()
        elif option == "2":
            update_quantity()
        elif option == "3":
            has_enough()
        elif option == "4":
            break
        else:
            print("Invalid option.\n")

menu()
