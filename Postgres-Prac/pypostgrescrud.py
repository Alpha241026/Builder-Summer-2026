from dotenv import load_dotenv
import os, psycopg2

load_dotenv()

def connect():
    connection =  psycopg2.connect(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("USER"),
        password=os.getenv("PASS")
    )
    
    print("database connection established")
    return connection

conn = connect()
cur = conn.cursor()

cur.execute("SELECT * FROM categories;")
rows = cur.fetchall()
print(rows)

cur.close()
conn.close()