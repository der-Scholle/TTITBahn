# trains.py - Deutsche Bahn Train Scheduler

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
    print(f"Train {train_number} added from main branch.\n")

def delete_train():
    train_number = input("Enter train number to delete: ")
    global trains
    new_trains = [t for t in trains if t["number"] != train_number]
    if len(new_trains) == len(trains):
        print("Train not found.\n")
    else:
        trains = new_trains
        print(f"Train {train_number} deleted.\n")

def search_by_route():
    route = input("Enter route (e.g., Berlin->Hamburg): ")
    found = [t for t in trains if route.lower() in t["route"].lower()]
    if found:
        for t in found:
            print(f"{t['number']}: {t['route']} at {t['departure']}")
    else:
        print("No trains found.\n")

def list_all_trains():
    if not trains:
        print("No trains in schedule.\n")
        return
    for t in trains:
        print(f"{t['number']} | {t['route']} | {t['departure']}")
    print()

def main():
    while True:
        print("\n1. Add train")
        print("2. Delete train")
        print("3. Search by route")
        print("4. List all trains")
        print("5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_train()
        elif choice == "2":
            delete_train()
        elif choice == "3":
            search_by_route()
        elif choice == "4":
            list_all_trains()
        elif choice == "5":
            break

if __name__ == "__main__":
    main()