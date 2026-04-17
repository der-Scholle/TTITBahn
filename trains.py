trains = []

def add_train():
    train_number = input("Train number: ")
    route = input("Route (e.g., Berlin->Hamburg): ")
    departure = input("Departure time: ")
    trains.append({
        "number": train_number,
        "route": route,
        "departure": departure
    })
    print(f"Train {train_number} added.\n")

def main():
    while True:
        print("\n1. Add train")
        print("2. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_train()
        elif choice == "2":
            break

if __name__ == "__main__":
    main()