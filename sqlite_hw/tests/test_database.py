import pprint

def test_full_data(database):
    cursor = database.cursor()
    result = cursor.execute("select * from Console_price where good_id >= 60;")
    pprint.pprint(result.fetchall())


