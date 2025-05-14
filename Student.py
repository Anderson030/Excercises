students = {}

def add_student():
    name = input("Enter student name: ").strip()
    if name not in students:
        students[name] = []
        print("Student added.\n")
    else:
        print("Student already exists.\n")

def add_grade():
    name = input("Enter student name: ").strip()
    if name in students:
        try:
            grade = float(input("Enter grade: "))
            students[name].append(grade)
            print("Grade added.\n")
        except ValueError:
            print("Invalid grade. Enter Grade \n")
    else:
        print("Student not found.\n")

def get_average():
    name = input("Enter student name: ").strip()
    if name in students and students[name]:
        avg = sum(students[name]) / len(students[name])
        print(f"Average grade: {avg:.2f}\n")
    else:
        print("Student not found or has no grades.\n")


def menu():
    while True:
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Get Average Grade")
        print("4. Exit")
        option = input("Select an option: ").strip()
        if option == "1":
            add_student()
        elif option == "2":
            add_grade()
        elif option == "3":
            get_average()
        elif option == "4":
            break
        else:
            print("Invalid option.\n")

menu()