import pytest
import sqlite3


@pytest.fixture
def database():
    connection = sqlite3.connect(
        r'C:\Users\Podli\OneDrive\Рабочий стол\Hillel\Hillel_Course_AQA_Podlinnov\sqlite_hw\Console_price.db',
        isolation_level=None)
    yield connection
    connection.close()
