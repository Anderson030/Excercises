expenses = []

def add_expense():
    category = input("Enter category (e.g. food, transport, etc.): ").strip()
    try:
        amount = float(input("Enter amount: "))
        expenses.append({"category": category, "amount": amount})
        print("Expense added.\n")
    except ValueError:
        print("Invalid amount.\n")

def total_spent():
    total = sum(e["amount"] for e in expenses)
    print(f"Total spent: ${total:.2f}\n")

def expense_percentages():
    total = sum(e["amount"] for e in expenses)
    if total == 0:
        print("No expenses recorded.\n")
        return

    category_totals = {}
    for e in expenses:
        category_totals[e["category"]] = category_totals.get(e["category"], 0) + e["amount"]

    for category, amount in category_totals.items():
        percent = (amount / total) * 100
        print(f"{category}: {percent:.2f}%")
    print()

# Example menu
def menu():
    while True:
        print("1. Add Expense")
        print("2. Total Spent")
        print("3. Expense Percentages")
        print("4. Exit")
        option = input("Choose an option: ").strip()
        if option == "1":
            add_expense()
        elif option == "2":
            total_spent()
        elif option == "3":
            expense_percentages()
        elif option == "4":
            break
        else:
            print("Invalid option.\n")

menu()
