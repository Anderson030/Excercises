courses = []

def add_course():
    title = input("Enter course title: ").strip()
    try:
        duration = int(input("Enter course duration (in hours): "))
        students = int(input("Enter number of enrolled students: "))
        courses.append({"title": title, "duration": duration, "students": students})
        print("Course added.\n")
    except ValueError:
        print("Invalid input. Please enter numbers for duration and students.\n")

def update_enrollment():
    title = input("Enter course title to update: ").strip()
    for course in courses:
        if course["title"].lower() == title.lower():
            try:
                new_enrollment = int(input("Enter new number of students: "))
                course["students"] = new_enrollment
                print("Enrollment updated.\n")
                return
            except ValueError:
                print("Invalid number.\n")
                return
    print("Course not found.\n")

def filter_by_hours():
    try:
        min_hours = int(input("Enter minimum course duration: "))
        filtered = [c for c in courses if c["duration"] >= min_hours]
        for course in filtered:
            print(course)
        if not filtered:
            print("No courses found with that duration.\n")
    except ValueError:
        print("Invalid number.\n")

# Example menu
def menu():
    while True:
        print("1. Add Course")
        print("2. Update Enrollment")
        print("3. Filter by Duration")
        print("4. Exit")
        option = input("Choose an option: ").strip()
        if option == "1":
            add_course()
        elif option == "2":
            update_enrollment()
        elif option == "3":
            filter_by_hours()
        elif option == "4":
            break
        else:
            print("Invalid option.\n")

menu()
