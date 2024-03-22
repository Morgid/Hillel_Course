import pprint
import sqlite3


def create_database():
    connection = sqlite3.connect("Console_price.db", isolation_level=None)
    cursor = connection.cursor()
    connection.execute(
        "CREATE TABLE IF NOT EXISTS Console_price(good_id INTEGER PRIMARY KEY, name TEXT, price_UAH REAL, quantity INTEGER);")

    with open('script.sql', 'r') as file:
        cursor.executescript(file.read())

    result = cursor.execute("select * from Console_price;")
    pprint.pprint(result.fetchall())

    cursor.close()
    connection.close()


create_database()
