from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

URL = "https://demoqa.com/checkbox"

class CheckboxPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(URL)
        return self

    def expand_folder_home(self, name) -> None:
        versatile_checkbox_button = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span/button")
        try:
            expand = versatile_checkbox_button.find_element(By.XPATH, "//*[contains(@class, 'expand-open')]")
            if expand.is_displayed():
                expand.click()
        except NoSuchElementException:
            pass
        versatile_checkbox_button.click()

    def expand_folder_other(self, name) -> None:
        versatile_checkbox_button = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span/button")
        versatile_checkbox_button.click()

    def collapse_folder(self, name) -> None:
        versatile_checkbox_button = self.driver.find_element(By.XPATH,
                                                             f"//label[contains(@for, 'tree-node-{name}')]//ancestor::span/button")
        try:
            expand = versatile_checkbox_button.find_element(By.XPATH, "//*[contains(@class, 'expand-close')]")
            if expand.is_displayed():
                expand.click()
        except NoSuchElementException:
            pass
        versatile_checkbox_button.click()


    def mark_folder(self, name):
        versatile_checkbox_button = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]")
        input_field = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]/input")
        if not input_field.is_selected():
            versatile_checkbox_button.click()


    def unmark_folder(self, name):
        versatile_checkbox_button = self.driver.find_element(By.XPATH, f"//label[contains(@for, 'tree-node-{name}')]")
        versatile_checkbox_button.click()

    def locator_success(self):
        locator_success = self.driver.find_elements(By.XPATH, '//*[@class="text-success"]')
        success_list = []
        for element in locator_success:
            text_value = element.text
            success_list.append(text_value)
        return success_list

    def scroll_down(self) -> None:
        self.driver.execute_script("window.scrollBy(0, 500);")