def test_table_data(table_cursor):
    table_cursor.execute('select id, name from items')
    data_from_table = table_cursor.fetchall()

    assert (1, "books") in data_from_table
