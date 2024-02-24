import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def firefox(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
