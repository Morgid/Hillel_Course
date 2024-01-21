import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    service = Service(executable_path='C:\Users\Podli\OneDrive\Рабочий стол\Hillel\Hillel_Course_AQA_Podlinnov\Lesson_20\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    # driver.close()  # закриває вкладку
    driver.quit()  # закриває браузер

@pytest.fixture
def firefox():
    service = Service(executable_path='C:\Users\Podli\OneDrive\Рабочий стол\Hillel\Hillel_Course_AQA_Podlinnov\Lesson_20\geckodriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    # driver.close()  # закриває вкладку
    driver.quit()  # закриває браузер