import pytest
import sqlite3


table_data = [(1, "books")]

@pytest.fixture(scope='session')
def connection():
    connection = sqlite3.connect('example.db')
    yield connection
    connection.close()

@pytest.fixture(scope='session')
def cursor(connection):
    cursor = connection.cursor()
    return cursor
    #cursor.close()

@pytest.fixture(scope='function')
@pytest.mark.parametrize("table_data", table_data)
def table_cursor(request, cursor):
    
    cursor.execute('drop table if exists items')
    cursor.execute('create table items (id int, name text)')
    for data in table_data:
        cursor.execute(f'insert into items values  {data}')
    cursor.connection.commit()

    yield cursor

    def teardown():
        cursor.execute('drop table if exists items')

    request.addfinalizer(teardown)
    

    
    
