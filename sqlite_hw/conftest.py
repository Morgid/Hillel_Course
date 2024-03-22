import pytest
import sqlite3


@pytest.fixture
def database():
    connection = sqlite3.connect('Console_price.db', isolation_level=None)
    yield connection
    connection.close()
