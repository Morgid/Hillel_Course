import pytest

from selenium.webdriver.common.by import By
from Hillel_Course_AQA_Podlinnov.Selenium.CheckboxPage_hw import CheckboxPage


@pytest.mark.usefixtures("firefox")
class TestCheckboxPage:
    def setup(self):
        self.page = CheckboxPage(self.driver)

    def test_page(self):
        self.page.open()
        self.page.scroll_down()
        self.page.expand_folder_home("home")
        self.page.mark_folder("home")
        self.page.collapse_folder("home")
        self.page.unmark_folder("home")

    def test_command_general(self):
        self.page.open()
        self.page.scroll_down()
        self.page.expand_folder_home("home")
        self.page.expand_folder_other("desktop")
        self.page.expand_folder_other("documents")
        self.page.expand_folder_other("office")
        self.page.mark_folder("commands")
        self.page.mark_folder("general")
        assert self.page.driver.find_element(By.XPATH, '//*[@class="text-success"]').is_displayed()
        assert "commands" in self.page.locator_success()
        assert "general" in self.page.locator_success()
