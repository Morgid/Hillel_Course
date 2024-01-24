import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="C:\Works\Other\AQA\Hillel_october_23-main\Selenium\chromedriver.exe")
    yield driver
    driver.quit()
