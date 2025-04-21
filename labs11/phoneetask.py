import psycopg2
import csv
import os

conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="109115"
)

def create_table():
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name TEXT,
            surname TEXT,
            phone TEXT
        )
    """)
    conn.commit()
    cur.close()

def insert_from_csv(phonebook):
    full_path = os.path.abspath(phonebook)
    print(f"I'm looking for a file on the path: {full_path}")

    if not os.path.isfile(phonebook):
        print(f"File '{phonebook}' not found.")
        return

    cur = conn.cursor()
    with open(phonebook, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute("SELECT * FROM phonebook WHERE phone = %s", (row[2],))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (row[0], row[1], row[2]))
            else:
                print(f"Number {row[2]} already exists — skipped.")
    conn.commit()
    cur.close()
    print("The import is completed (duplicates skipped).")

def insert_manual():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone: ")
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook(name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
    conn.commit()
    cur.close()
    print("User inserted.")

def insert_many():
    count = int(input("How many users? "))
    data = []
    for _ in range(count):
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        data.append(f"{name},{surname},{phone}")
    cur = conn.cursor()
    cur.execute("CALL insert_many_users(%s)", (data,))
    conn.commit()
    cur.close()
    print("Users inserted.")

def update_entry():
    user_id = int(input("Enter user ID to update: "))
    name = input("New name: ")
    surname = input("New surname: ")
    phone = input("New phone: ")
    cur = conn.cursor()
    cur.execute("CALL update_user(%s, %s, %s, %s)", (user_id, name, surname, phone))
    conn.commit()
    cur.close()
    print("Entry updated.")

def paginate_results():
    limit = int(input("Enter limit (how many rows per page): "))
    offset = int(input("Enter offset (how many rows to skip): "))
    cur = conn.cursor()
    cur.execute("SELECT * FROM paginate_users(%s, %s)", (limit, offset))
    for row in cur.fetchall():
        print(row)
    cur.close()

def search_by_pattern():
    field = input("Search field (name/surname/phone): ")
    pattern_type = input("Pattern type (contains/start/end/exact): ")
    pattern = input("Enter pattern value: ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_by_pattern(%s, %s, %s)", (field, pattern_type, pattern))
    for row in cur.fetchall():
        print(row)
    cur.close()

def delete_by_field():
    show_all()
    field = input("Field to delete by (name/surname/phone): ")
    value = input("Value: ")
    cur = conn.cursor()
    cur.execute("CALL delete_by_field(%s, %s)", (field, value))
    conn.commit()
    cur.close()
    print("Entry deleted.")

def show_all():
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)
    cur.close()

def menu():
    create_table()
    while True:
        print("\nMenu:")
        print("1. Insert from CSV")
        print("2. Insert manually")
        print("3. Insert many users")
        print("4. Update entry")
        print("5. Paginate results")
        print("6. Search by pattern")
        print("7. Delete by name/surname/phone")
        print("8. Show all")
        print("9. Exit")
        choice = input("Choose an action: ")
        
        if choice == '1':
            filename = input("Enter CSV file name (e.g. phonebook.csv): ")
            insert_from_csv(filename)
        elif choice == '2':
            insert_manual()
        elif choice == '3':
            insert_many()
        elif choice == '4':
            update_entry()
        elif choice == '5':
            paginate_results()
        elif choice == '6':
            search_by_pattern()
        elif choice == '7':
            delete_by_field()
        elif choice == '8':
            show_all()
        elif choice == '9':
            break
        else:
            print("Invalid choice!")

menu()
