import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="C:\Users\Podli\OneDrive\Рабочий стол\Hillel\Hillel_Course_AQA_Podlinnov\lesson_21\chromedriver.exe")
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def firefox(request):
    driver = webdriver.Firefox(executable_path="C:\Users\Podli\OneDrive\Рабочий стол\Hillel\Hillel_Course_AQA_Podlinnov\lesson_21\geckodriver.exe")
    request.cls.driver = driver
    driver.implicitly_wait(5)  # імплісіті вейт це вся реалізація
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome(executable_path="C:\\Users\\Podli\\OneDrive\\Рабочий стол\\Hillel\\Hillel_Course_AQA_Podlinnov\\Selenium\\chromedriver.exe")
    request.cls.driver = driver
    yield driver
    driver.quit()
