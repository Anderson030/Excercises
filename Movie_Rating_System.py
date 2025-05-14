movies = {}

def add_movie():
    name = input("Enter movie name: ").strip()
    if name not in movies:
        movies[name] = []
        print("Movie added.\n")
    else:
        print("Movie already exists.\n")

def rate_movie():
    name = input("Enter movie to rate: ").strip()
    if name in movies:
        try:
            rating = int(input("Enter rating (1–5): "))
            if 1 <= rating <= 5:
                movies[name].append(rating)
                print("Rating added.\n")
            else:
                print("Rating must be between 1 and 5.\n")
        except ValueError:
            print("Invalid rating. Must be a number.\n")
    else:
        print("Movie not found.\n")

def average_rating():
    name = input("Enter movie name to calculate average: ").strip()
    if name in movies and movies[name]:
        avg = sum(movies[name]) / len(movies[name])
        print(f"Average rating: {avg:.2f}\n")
    else:
        print("Movie not found or has no ratings.\n")

# Example menu
def menu():
    while True:
        print("1. Add Movie")
        print("2. Rate Movie")
        print("3. Show Average Rating")
        print("4. Exit")
        option = input("Choose an option: ").strip()
        if option == "1":
            add_movie()
        elif option == "2":
            rate_movie()
        elif option == "3":
            average_rating()
        elif option == "4":
            break
        else:
            print("Invalid option.\n")

menu()
