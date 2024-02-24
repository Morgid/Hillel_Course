from selenium.webdriver.remote.webelement import WebElement

from Hillel_Course_AQA_Podlinnov.site_locators.ElementsPage import ElementsPage


class TestElementsPage:
    def test_button_profit_xpath_full(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        profit_xfull: WebElement = page.button_profit_xpath_full()
        profit_xfull.click()

    def test_button_profit_xpath_short(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        profit_xshort: WebElement = page.button_profit_xpath_short()
        profit_xshort.click()

    def test_search_input_xpath(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        page.search_input_xpath('Лопата')

    def test_swipper_button_xpath(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        swipper_xpath: WebElement = page.swipper_button_xpath()
        swipper_xpath.click()

    def test_link_garden_xpath(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        catalog: WebElement = page.catalog_menu_css()
        catalog.click()
        link_xpath: WebElement = page.link_garden_xpath()
        link_xpath.click()

    def test_catalog_menu_css(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        catalog: WebElement = page.catalog_menu_css()
        catalog.click()

    def test_search_input_css(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        page.search_input_css('Лопата з ручкою')

    def test_button_profit_css(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        profit_c: WebElement = page.button_profit_css()
        profit_c.click()

    def test_button_profit_css_by_link(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        profit_link: WebElement = page.button_profit_css_by_link()
        profit_link.click()

    def test_back_button_loc(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        profit_link: WebElement = page.back_button()
        profit_link.click()
