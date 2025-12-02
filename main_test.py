from src.player_database import PlayerDatabase

def run_tests():
    print("=== Running NBA Player Database Tests ===")

    db = PlayerDatabase()
    db.load_data("data/nba_players.csv")

    print("\n1. Dataset Loaded")
    print("Players loaded:", db.count)

    print("\n2. Show Head")
    print(db.show_head(3))

    print("\n3. Show Tail")
    print(db.show_tail(3))

    print("\n4. Summary Stats")
    print(db.summary_statistics())

    print("\n5. Search for 'James'")
    print(db.search_by_name("James"))

    print("\n6. Age filter 20–25")
    print(db.filter_by_age(20, 25))

    print("\n7. Top salaries")
    print(db.top_salaries(5))

    print("\nAll tests completed.")

if __name__ == "__main__":
    run_tests()
