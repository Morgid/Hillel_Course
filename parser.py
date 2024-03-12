from selenium import webdriver
from selenium.webdriver.common.by import By


def parser():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.get('https://rozetka.com.ua/consoles/c80020/')
    goods_name_all = driver.find_elements(By.XPATH, "//*[@class='goods-tile__title']")
    goods_value_all = driver.find_elements(By.XPATH, "//span[@class='goods-tile__price-value']")
    next_page = driver.find_elements(By.XPATH, "//ul[@class='pagination']//a[text()='2']")

    goods_value = []
    goods_name = []

    for good in goods_name_all:
        goods_name.append(good.text)
    for price in goods_value_all:
        goods_value.append(price.text)
    goods_name_value = dict(zip(goods_name, goods_value))
    driver.quit()
    return goods_name_value



def write_to_file():
    page_info = parser()
    with open('Game_page_parse.txt', 'w', encoding='utf-8') as file:
        goods_name_value_info = ''
        for key, value in page_info.items():
            goods_name_value_info += f'{key} - {value} \n'
        file.write(goods_name_value_info)


write_to_file()
