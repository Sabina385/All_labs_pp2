import psycopg2
import csv
import os

def connect():
    return psycopg2.connect(
        host="localhost",
        database="phonebook",
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

    # Проверка на дубликат по номеру
    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
        conn.commit()
        print("Added successfully.")
    else:
        print("Such a number already exists. The entry has not been added.")

    cur.close()
    conn.close()

def show_all():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

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

def search():
    show_all()
    choice = input("Search by name (1) or phone (2)? ")
    conn = connect()
    cur = conn.cursor()
    if choice == '1':
        value = input("Enter name: ")
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (value,))
    else:
        value = input("Enter phone: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (value,))
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    conn.close()

def delete():
    show_all()
    user_id = input("Enter ID to delete: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE id = %s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()
    print("Deleted.")

def menu():
    create_table()
    while True:
        print("\nMenu:")
        print("1. Insert from CSV")
        print("2. Insert manually")
        print("3. Update entry")
        print("4. Search")
        print("5. Delete")
        print("6. Show all")
        print("7. Exit")
        choice = input("Choose an action: ")

        if choice == '1':
            filename = input("Enter CSV file name (e.g. phonebook.csv): ")
            insert_from_csv(filename)
        elif choice == '2':
            insert_manual()
        elif choice == '3':
            update_entry()
        elif choice == '4':
            search()
        elif choice == '5':
            delete()
        elif choice == '6':
            show_all()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Wrong choice. Try again.")

if __name__ == "__main__":
    menu()