import pytest
from selenium import webdriver


# from selenium.webdriver.chrome.service import Service - щоб запускати хром з екзекютебл пасом

@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# щоб запускати хром з екзекютебл пасом
# @pytest.fixture
# def chrome():
#     service = Service(
#         executable_path='C:\AQA\Hillel_Course_AQA_Podlinnov\Selenium\chromedriver.exe')
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(service=service, options=options)
#     yield driver
#     driver.quit()

@pytest.fixture(scope="class")
def firefox(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield driver
    driver.quit()
