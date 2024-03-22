import sqlite3

from Hillel_Course_AQA_Podlinnov.sqlite_hw.Database_from_parser.parser_pages_Rozetka import ParserRozetka

connection = sqlite3.connect("Console_price_from_parser.db",
                             isolation_level=None)
cursor = connection.cursor()

connection.execute(
    "CREATE TABLE IF NOT EXISTS Console_price(good_id INTEGER PRIMARY KEY, name TEXT, price_USD REAL, price_UAH REAL);")

parser = ParserRozetka()
parser.choose_category()
values = parser.collect_info()
curs_dollar = 39.15
for key, value in values.items():
    value = (value.replace(' ', '').replace('₴', ''))
    result = cursor.execute("INSERT INTO Console_price (name, price_USD, price_UAH) VALUES ((?), (?), (?))",
                            (key, round((int(value) / curs_dollar), 2), value))

result = cursor.execute("select * from Console_price;")
for i in result:
    print(f'{i}')

cursor.close()
connection.close()
