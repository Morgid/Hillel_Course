def test_all_data(database):
    cursor = database.cursor()
    cursor.execute("select count(*) from Console_price;")
    count = cursor.fetchone()[0]
    assert count == 4


def test_id_data(database):
    cursor = database.cursor()
    cursor.execute(f'select * from Console_price where good_id == (?);', (4,))
    result = cursor.fetchall()
    assert result == [(4, 'Microsoft Xbox Series S 1TB', 17999.5, 0)]
