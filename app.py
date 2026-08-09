import sqlite3

# Create Database Connection
conn = sqlite3.connect("emergency_resources.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    name TEXT,
    location TEXT,
    contact TEXT
)
""")

conn.commit()

def add_resource():
    resource_type = input("Enter Resource Type (Hospital/Ambulance/Blood Bank): ")
    name = input("Enter Resource Name: ")
    location = input("Enter Location: ")
    contact = input("Enter Contact Number: ")

    cursor.execute(
        "INSERT INTO resources(type, name, location, contact) VALUES (?, ?, ?, ?)",
        (resource_type, name, location, contact)
    )

    conn.commit()
    print("\nResource Added Successfully!")

def search_resource():
    resource_type = input("\nEnter Resource Type to Search: ")

    cursor.execute(
        "SELECT * FROM resources WHERE type=?",
        (resource_type,)
    )

    results = cursor.fetchall()

    if results:
        print("\nAvailable Resources")
        print("-" * 50)

        for row in results:
            print(f"ID: {row[0]}")
            print(f"Type: {row[1]}")
            print(f"Name: {row[2]}")
            print(f"Location: {row[3]}")
            print(f"Contact: {row[4]}")
            print("-" * 50)
    else:
        print("No resources found.")

def view_all():
    cursor.execute("SELECT * FROM resources")
    rows = cursor.fetchall()

    print("\nAll Emergency Resources")
    print("-" * 50)

    for row in rows:
        print(row)

def main():
    while True:
        print("\n===== AI National Emergency Resource Brain =====")
        print("1. Add Resource")
        print("2. Search Resource")
        print("3. View All Resources")
        print("4. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_resource()

        elif choice == "2":
            search_resource()

        elif choice == "3":
            view_all()

        elif choice == "4":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()

conn.close()
