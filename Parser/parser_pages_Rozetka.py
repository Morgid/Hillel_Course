from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ParserRozetka:
    URL = 'https://rozetka.com.ua'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url=self.URL)

        self.category_main_loc = By.XPATH, "//*[@class='menu-categories__link'][contains(text(), 'Товари для геймерів')]"
        self.category_loc = By.XPATH, "//*//a[contains(text(), 'Ігрові приставки')]"

        self.goods_name_all_loc = By.XPATH, "//*[@class='goods-tile__title']"
        self.goods_value_all_loc = By.XPATH, "//span[@class='goods-tile__price-value']"

        self.next_page_loc = By.XPATH, "//*[@class='pagination__link ng-star-inserted'][contains(text(), '2')]"
        self.next_page_clicked_loc = By.XPATH, "//h1[contains(text(), 'Ігрові приставки')]"

    def choose_category(self):
        self.category_main = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.category_main_loc))
        self.category_main.click()
        category = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.category_loc))
        category.click()

    def next_page(self):
        self.next_page_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.next_page_loc))
        self.driver.execute_script("arguments[0].scrollIntoView();", self.next_page_element)
        self.next_page_element.click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.next_page_clicked_loc))

    def collect_info(self):
        goods_name = []
        goods_value = []
        for good in self.driver.find_elements(*self.goods_name_all_loc):
            goods_name.append(good.text)
        for price in self.driver.find_elements(*self.goods_value_all_loc):
            goods_value.append(price.text)
        goods_name_value = dict(zip(goods_name, goods_value))
        return goods_name_value

    def write_parsed_page(self):
        self.choose_category()
        with open('Game_page_parse.txt', 'w', encoding='utf-8') as file:
            parsed_page_1 = ''
            for key, value in self.collect_info().items():
                parsed_page_1 += f'{key} - {value} \n'
            self.next_page()
            parsed_page_2 = ''
            for key, value in self.collect_info().items():
                parsed_page_2 += f'{key} - {value} \n'
            file.write(f"{'=' * 20} Перша сторінка {'=' * 20} \n"
                       f"{parsed_page_1} \n"
                       f"{'=' * 20} Друга сторінка {'=' * 20} \n"
                       f"{parsed_page_2}")
        self.driver.quit()


ParserRozetka().write_parsed_page()
