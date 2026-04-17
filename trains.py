# trains.py - Deutsche Bahn Train Scheduler

trains = []

def delete_train():
    train_number = input("Enter train number to delete: ")
    global trains
    new_trains = [t for t in trains if t["number"] != train_number]
    if len(new_trains) == len(trains):
        print("Train not found.\n")
    else:
        trains = new_trains
        print(f"Train {train_number} deleted.\n")

def main():
    while True:
        print("\n1. Delete train")
        print("2. Exit")
        choice = input("Choose: ")
        if choice == "1":
            delete_train()
        elif choice == "2":
            break

if __name__ == "__main__":
    main()