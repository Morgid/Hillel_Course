# import sqlite3
# import pprint
#
# class Vendor:
#     def __init__(self, good_id, name, qantity, price):
#         self.good_id = good_id
#         self.name = name
#         self.qantity = qantity
#         self.price = price
#
#
#     def __repr__(self):
#         return f"Vendor(good_id={self.good_id}, name={self.name}, qantity={self.qantity}, price={self.price})"
#
# class AbstractRepository:
#     def __init__(self, db_path):
#         self._connection = sqlite3.connect(db_path, isolation_level=None)
#         self._cursor = self._connection.cursor()
#
#     def __del__(self):
#         if self._cursor:
#             self._cursor.close()
#         if self._connection:
#             self._connection.close()
#
# class VendorsRepository(AbstractRepository):
#     def __init__(self, db_path):
#         super().__init__(db_path)
#         with open('script.sql', 'r') as f:
#             self._cursor.executescript(f.read())
#
# vendor_repo = VendorsRepository('Console_price.db')
#
# vendor_repo._cursor.execute(f'select * from Console_price;')
# pprint.pprint(vendor_repo.fetchall())
# print(vendor_repo.fetchall())
#
#
# # def cteate_db(db_path):
# #     connection = sqlite3.connect(db_path, isolation_level=None)
# #     cursor = connection.cursor()
# #
# #     with open('script.sql', 'r') as f:
# #         cursor.executescript(f.read())
#
# # result = cursor.execute('select.... from db')
# # connection.commit()
#
# # cursor.close()
# # connection.close()

import sqlite3
from Hillel_Course_AQA_Podlinnov.Parser.parser_pages_Rozetka import ParserRozetka
connection = sqlite3.connect(r"C:\Users\Podli\OneDrive\Рабочий стол\Hillel\Hillel_Course_AQA_Podlinnov\sqlite_hw\Console_price.db", isolation_level=None)  # isolation_level=None - потрібен що б відразу комітило
cursor = connection.cursor()

import pprint




values = ParserRozetka().collect_info()
# print(values)
for key, value in values:
    result = cursor.execute(f"INSERT INTO Console_price(name, price) VALUES ('{key}', {values};")

# cursor.executemany(f"INSERT INTO Console_price(name, qantity, price) VALUES ((?), (?), (?));",
#                   [('Pavlo21', 'Car-sedan44', 4, 101),
#                    ('Pavlo11', 'Car-sedan56', 4, 102),
#                    ('Pavlo1', 'Car-sedan67', 4, 101)])

result = cursor.execute(f'select * from Console_price;')
pprint.pprint(list(result))