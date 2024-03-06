import pytest

from selenium.webdriver.remote.webelement import WebElement

from Hillel_Course_AQA_Podlinnov.Selenium.DynamicPropertiesPage import PageDynamicProperties
from Hillel_Course_AQA_Podlinnov.Selenium.ElementsPage import ElementsPage


class TestElementsPage:

    def test_page(self, chrome):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert len(elements) == 33

    @pytest.mark.parametrize('elements_all',
                             ['Text Box', 'Check Box', 'Radio Button', 'Web Tables', 'Buttons', 'Links',
                              'Broken Links - Images', 'Upload and Download', 'Dynamic Properties', '', '', '', '', '',
                              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])
    def test_page_elements_all(self, chrome, elements_all):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert elements_all in elements

    def test_is_button_enabled(self, chrome):
        page = PageDynamicProperties(chrome)
        page.open()
        button: WebElement = page.disable_enable_button()
        button.click()

    def test_is_button_shown(self, chrome):
        page = PageDynamicProperties(chrome).open()  # короткий запис
        button: WebElement = page.button_invisible_visible()
        button.click()
