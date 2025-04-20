import psycopg2
import csv
import os

def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="109115"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            surname VARCHAR(100),
            phone VARCHAR(20) UNIQUE
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(phonebook):
    full_path = os.path.abspath(phonebook)
    print(f" I'm looking for a file on the path:{full_path}")

    if not os.path.isfile(phonebook):
        print(f"File '{phonebook}' not found.")
        return

    conn = connect()
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
    conn.close()
    print("The import is completed (duplicates by number are skipped).")

def insert_manual():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
        conn.commit()
        print("Added successfully.")
    else:
        print("Such a number already exists. The entry has not been added.")

    cur.close()
    conn.close()

def insert_many():
    users = []
    count = int(input("How many users do you want to add? "))
    for _ in range(count):
        name = input("Name: ")
        surname=input("Surname:")
        phone = input("Phone: ")
        users.append((name,surname, phone))

    incorrect = []
    conn = connect()
    cur = conn.cursor()

    for name, phone in users:
        if not phone.isdigit() or len(phone) < 5:
            incorrect.append((name, phone))
            continue

        cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
        if cur.fetchone():
            cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
        else:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()

    if incorrect:
        print("Incorrect entries:")
        for i in incorrect:
            print(i)
    else:
        print("All users inserted/updated successfully.")

def update_entry():
    show_all()
    user_id = input("Enter ID to update: ")
    choice = input("What to update? (1 - name, 2 - surname, 3 - phone): ")

    conn = connect()
    cur = conn.cursor()
    if choice == '1':
        new_value = input("New name: ")
        cur.execute("UPDATE phonebook SET name = %s WHERE id = %s", (new_value, user_id))
    elif choice == '2':
        new_value = input("New surname: ")
        cur.execute("UPDATE phonebook SET surname = %s WHERE id = %s", (new_value, user_id))
    elif choice == '3':
        new_value = input("New phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (new_value,))
        if cur.fetchone() is None:
            cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (new_value, user_id))
        else:
            print("Such a number already exists. The update has been canceled.")
    conn.commit()
    cur.close()
    conn.close()
    print("The update is complete.")

def search_by_pattern():
    print("Search by:")
    print("1 - Name")
    print("2 - Surname")
    print("3 - Phone")
    field_choice = input("Choose a field: ")
    print("Pattern type:")
    print("1 - Contains")
    print("2 - Starts with")
    print("3 - Ends with")
    print("4 - Exact match")
    pattern_choice = input("Choose pattern type: ")
    value = input("Enter value to search: ")

    field = "name" if field_choice == '1' else "surname" if field_choice == '2' else "phone"
    if pattern_choice == '1':
        pattern = f"%{value}%"
    elif pattern_choice == '2':
        pattern = f"{value}%"
    elif pattern_choice == '3':
        pattern = f"%{value}"
    else:
        pattern = value

    conn = connect()
    cur = conn.cursor()
    query = f"SELECT * FROM phonebook WHERE {field} ILIKE %s"
    cur.execute(query, (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def paginate():
    limit = int(input("Enter limit (how many rows per page): "))
    offset = int(input("Enter offset (how many rows to skip): "))
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_entry():
    print("Delete by:")
    print("1 - Name")
    print("2 - Surname")
    print("3 - Phone")
    choice = input("Choose: ")
    value = input("Enter value: ")

    field = "name" if choice == '1' else "surname" if choice == '2' else "phone"
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonebook WHERE {field} = %s", (value,))
    conn.commit()
    cur.close()
    conn.close()
    print("Deleted.")

def show_all():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

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
            paginate()
        elif choice == '6':
            search_by_pattern()
        elif choice == '7':
            delete_entry()
        elif choice == '8':
            show_all()
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Wrong choice. Try again.")

if __name__ == "__main__":
    menu()








