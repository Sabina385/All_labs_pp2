
import psycopg2

def drop_tables():
    conn = psycopg2.connect(
        dbname="snakegame",
        user="postgres",
        password="109115",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    
    # Удаляем таблицы, если они существуют
    cur.execute("DROP TABLE IF EXISTS scores CASCADE;")
    cur.execute("DROP TABLE IF EXISTS users CASCADE;")
    
    conn.commit()
    cur.close()
    conn.close()
    print("Таблицы успешно удалены.")

drop_tables()

