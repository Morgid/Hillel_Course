from selenium.webdriver.common.by import By


class ElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://epicentrk.ua/"
        self.button_profit_xpath_full_loc = By.XPATH, '//*[@id="global-site-header"]/header/div/div[8]/div/div[3]/ul/li/a'
        self.button_profit_xpath_short_loc = By.XPATH, '//a[@title="Вигода"]'
        self.search_input_xpath_loc = By.XPATH, '//input[@class="_JcImSJ"]'
        self.swipper_button_xpath_loc = By.XPATH, '//div[@class="swiper-button-next"]'
        self.link_garden_xpath_loc = By.XPATH, '//a[@class="menu-link" and @href="https://epicentrk.ua/ua/shop/dacha-sad-i-ogorod/"]'
        self.catalog_menu_css_loc = By.CSS_SELECTOR, 'div.header__menu-opener-button-text'
        self.search_input_css_loc = By.CSS_SELECTOR, 'input[placeholder = "Пошук"]'
        self.button_profit_css_loc = By.CSS_SELECTOR, '#global-site-header > header > div > div.header__group > div > div.header__service-menu > ul > li > a'
        self.button_profit_css_by_link_loc = By.CSS_SELECTOR, 'a[link="/ua/vygoda/"]'
        self.back_button_loc = By.CSS_SELECTOR, 'div[data-is="ScrollTop"]'

    def open(self):
        self.driver.get(self.url)
        return self

    def scroll_down(self) -> None:
        self.driver.execute_script("window.scrollBy(0, 900);")

    def button_profit_xpath_full(self):
        return self.driver.find_element(*self.button_profit_xpath_full_loc)

    def button_profit_xpath_short(self):
        return self.driver.find_element(*self.button_profit_xpath_full_loc)

    def search_input_xpath(self, text: str):
        self.driver.find_element(*self.search_input_xpath_loc).send_keys(text)

    def swipper_button_xpath(self):
        return self.driver.find_element(*self.swipper_button_xpath_loc)

    def link_garden_xpath(self):
        return self.driver.find_element(*self.link_garden_xpath_loc)

    def catalog_menu_css(self):
        return self.driver.find_element(*self.catalog_menu_css_loc)

    def search_input_css(self, text: str):
        self.driver.find_element(*self.search_input_css_loc).send_keys(text)

    def button_profit_css(self):
        return self.driver.find_element(*self.button_profit_css_loc)

    def button_profit_css_by_link(self):
        return self.driver.find_element(*self.button_profit_css_by_link_loc)

    def back_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(*self.back_button_loc)
