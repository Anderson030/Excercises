members = []

def register_member():
    name = input("Enter member name: ").strip()
    plan = input("Enter membership plan (basic/premium): ").strip().lower()
    try:
        has_paid = input("Has the member paid? (yes/no): ").strip().lower() == "yes"
        members.append({"name": name, "plan": plan, "paid": has_paid})
        print("Member registered.\n")
    except:
        print("Error registering member.\n")

def change_plan():
    name = input("Enter member name to update: ").strip()
    for member in members:
        if member["name"].lower() == name.lower():
            new_plan = input("Enter new plan (basic/premium): ").strip().lower()
            member["plan"] = new_plan
            print("Plan updated.\n")
            return
    print("Member not found.\n")

def unpaid_members():
    found = [m for m in members if not m["paid"]]
    if found:
        print("Members with unpaid fees:")
        for m in found:
            print(m)
    else:
        print("All members are up to date.\n")

# Example menu
def menu():
    while True:
        print("1. Register Member")
        print("2. Change Plan")
        print("3. List Unpaid Members")
        print("4. Exit")
        option = input("Choose an option: ").strip()
        if option == "1":
            register_member()
        elif option == "2":
            change_plan()
        elif option == "3":
            unpaid_members()
        elif option == "4":
            break
        else:
            print("Invalid option.\n")

menu()
