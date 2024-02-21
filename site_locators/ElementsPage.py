from selenium.webdriver.common.by import By


class ElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.ukrposhta.ua/ua"
        self.element_categories = By.XPATH, f'//*[@id="main"]/div/div[4]/div/div/div/div/div/a'

    def open(self):
        self.driver.get(self.url)
        return self

    def get_elements_page_categories(self):
        categories = [cat.text for cat in self.driver.find_elements(*self.element_categories)]
        return categories



