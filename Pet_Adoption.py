pets = []

def add_pet():
    name = input("Enter pet name: ").strip()
    species = input("Enter species (e.g. dog, cat): ").strip()
    try:
        age = int(input("Enter age in years: "))
        pets.append({"name": name, "species": species, "age": age})
        print("Pet added.\n")
    except ValueError:
        print("Invalid age.\n")

def find_by_species():
    search_species = input("Enter species to search: ").strip().lower()
    found = [pet for pet in pets if pet["species"].lower() == search_species]
    if found:
        for pet in found:
            print(pet)
    else:
        print("No pets found for that species.\n")

def older_than():
    try:
        min_age = int(input("Show pets older than: "))
        found = [pet for pet in pets if pet["age"] > min_age]
        if found:
            for pet in found:
                print(pet)
        else:
            print("No pets found older than that age.\n")
    except ValueError:
        print("Invalid age.\n")

# Example menu
def menu():
    while True:
        print("1. Add Pet")
        print("2. Find by Species")
        print("3. Filter by Age")
        print("4. Exit")
        option = input("Choose an option: ").strip()
        if option == "1":
            add_pet()
        elif option == "2":
            find_by_species()
        elif option == "3":
            older_than()
        elif option == "4":
            break
        else:
            print("Invalid option.\n")

menu()
