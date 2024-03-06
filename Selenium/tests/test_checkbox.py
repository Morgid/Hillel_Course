import pytest
from Hillel_Course_AQA_Podlinnov.Selenium.CheckboxPage import CheckboxPage


@pytest.mark.usefixtures("chrome_class")
class TestCheckboxPage:
    def setup(self):
        self.page = CheckboxPage(self.driver)

    def test_page(self):
        self.page.open()
        self.page.expand_folder("home")
        self.page.mark_folder("home")
        self.page.collapse_folder("home")
        self.page.unmark_folder("home")
        pass

    # def test_page_command(self):
    #     self.page.open()
    #     self.page.expand_folder("all")
    #     self.page.expand_folder("desktop")
    #     self.page.collapse_folder("desktop")
    #     self.page.mark_folder("commands")
    #     self.page.unmark_folder("commands")
    #     pass
