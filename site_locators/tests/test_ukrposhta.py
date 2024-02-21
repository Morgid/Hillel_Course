import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class ElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.ukrposhta.ua/ua"
        self.button_orange_loc = By.XPATH, f'//*[@id="main"]/div/div[4]/div/div/div/div/div/a'

    def open(self):
        self.driver.get(self.url)
        return self

    def button_orange_need(self):
        self.driver.find_element(*self.button_orange_loc).click()

    def scroll_down(self) -> None:
        self.driver.execute_script("window.scrollBy(0, 500);")


def test_button(chrome):
    page = ElementsPage(chrome)
    page.open()
    page.scroll_down()
    page.button_orange_need()
    pass