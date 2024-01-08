import pytest
from selenium import webdriver


@pytest.fixture
def chrome():
    driver = webdriver.Chrome(
        executable_path="Users\Podli\OneDrive\Рабочий стол\Hillel\Hillel_Course_AQA_Podlinnov\Lesson_17\chromedriver.exe")
    yield driver
    # driver.close()  # закриває вкладку
    driver.quit()  # закриває браузер
