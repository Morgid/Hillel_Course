import pytest

from Hillel_Course_AQA_Podlinnov.Selenium.CheckboxPage_hw import CheckboxPage


@pytest.mark.usefixtures("chrome")
class TestCheckboxPage:
    def test_page(self, request):
        self.page = CheckboxPage(request.getfixturevalue("chrome"))
        self.page.open()
        self.page.expand_folder_home("home")
        self.page.mark_folder("home")
        self.page.collapse_folder("home")
        self.page.unmark_folder("home")

    def test_command_office(self, request):
        self.page = CheckboxPage(request.getfixturevalue("chrome"))
        self.page.open()
        self.page.expand_folder_home("home")
        self.page.expand_folder_other("desktop")
        self.page.expand_folder_other("documents")
        self.page.mark_folder("commands")
        self.page.mark_folder("office")
        assert "commands" in self.page.locator_success()
        assert "office" in self.page.locator_success()
