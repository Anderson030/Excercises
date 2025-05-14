tasks = []

def add_task():
    title = input("Enter task title: ").strip()
    priority = input("Enter priority (low/medium/high): ").strip().lower()
    tasks.append({"title": title, "priority": priority, "done": False})
    print("Task added.\n")

def complete_task():
    title = input("Enter task title to mark as done: ").strip()
    for task in tasks:
        if task["title"].lower() == title.lower():
            task["done"] = True
            print("Task marked as completed.\n")
            return
    print("Task not found.\n")

def filter_tasks():
    print("Filter by:")
    print("1. Priority")
    print("2. Completion Status")
    choice = input("Choose an option: ").strip()
    
    if choice == "1":
        level = input("Enter priority (low/medium/high): ").strip().lower()
        filtered = [t for t in tasks if t["priority"] == level]
    elif choice == "2":
        status = input("Completed? (yes/no): ").strip().lower()
        is_done = status == "yes"
        filtered = [t for t in tasks if t["done"] == is_done]
    else:
        print("Invalid option.\n")
        return

    if filtered:
        for t in filtered:
            print(t)
    else:
        print("No tasks found.\n")

# Example menu
def menu():
    while True:
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Filter Tasks")
        print("4. Exit")
        option = input("Choose an option: ").strip()
        if option == "1":
            add_task()
        elif option == "2":
            complete_task()
        elif option == "3":
            filter_tasks()
        elif option == "4":
            break
        else:
            print("Invalid option.\n")

menu()
