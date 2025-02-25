import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("chrome_class")
class TestWaiters:

    def test_connection(self):
        self.driver.get("https://demoqa.com/dynamic-properties")
        visible_invisible_button_loc = (By.CSS_SELECTOR, "#visibleAfter")  # = (By.ID, "visibleAfter")
        WebDriverWait(self.driver, timeout=5).until(ec.visibility_of_element_located(visible_invisible_button_loc))
        visible_invisible_button = self.driver.find_element(*visible_invisible_button_loc)
        visible_invisible_button.click()
        assert visible_invisible_button.is_displayed()

    def test_connection_enable(self):
        self.driver.get("https://demoqa.com/dynamic-properties")
        enable_button_loc = (By.CSS_SELECTOR, "#enableAfter")
        enable_button: WebElement = self.driver.find_element(*enable_button_loc)
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(enable_button_loc))
        enable_button.click()
        assert enable_button.is_enabled()

    def test_connection_color(self):
        self.driver.get("https://demoqa.com/dynamic-properties")
        colored_button_loc = (By.ID, "colorChange")
        colored_button: WebElement = self.driver.find_element(*colored_button_loc)
        WebDriverWait(self.driver, 10).until(
            ec.text_to_be_present_in_element_attribute(colored_button_loc, "class", "text-danger"))
        colored_button_loc.click()
        assert colored_button.is_enabled()
