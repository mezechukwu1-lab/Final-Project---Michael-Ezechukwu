from src.player_database import PlayerDatabase

def menu():
    print("\n--- NBA Player Database ---")
    print("1. Search player by name")
    print("2. Filter players by age range")
    print("3. Show top salaries")
    print("4. Show head")
    print("5. Show tail")
    print("6. Show summary statistics")
    print("0. Exit")
    return input("Choose an option: ")

def main():
    db = PlayerDatabase()
    db.load_data("data/nba_players.csv")

    while True:
        choice = menu()

        if choice == "1":
            name = input("Enter player name: ")
            print(db.search_by_name(name))

        elif choice == "2":
            min_age = int(input("Min age: "))
            max_age = int(input("Max age: "))
            print(db.filter_by_age(min_age, max_age))

        elif choice == "3":
            n = int(input("How many top salaries? "))
            print(db.top_salaries(n))

        elif choice == "4":
            print(db.show_head())

        elif choice == "5":
            print(db.show_tail())

        elif choice == "6":
            print(db.summary_statistics())

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
