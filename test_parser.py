
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_basic_service():
    service = webdriver.ChromeService()
    driver = webdriver.Chrome(service=service)
    driver.get('https://rozetka.com.ua/consoles/c80020/')
    goods_name_all = driver.find_elements(By.XPATH, "//*[@class='goods-tile__title']")
    goods_value_all = driver.find_elements(By.XPATH, "//span[@class='goods-tile__price-value']")
    with open('Game_page_parse.txt', 'w', encoding='utf-8') as file:
        goods_name_value = ''
        for good in goods_name_all:
            goods_name_value += f'{good.text} \n'
            for price in goods_value_all:
                goods_name_value += f' - {price.text} \n'
        file.write(goods_name_value)



    # driver.implicitly_wait(5)
    # element_click = driver.find_element(*goods_name)
    driver.quit()


# def test_driver_location(chromedriver_bin, chrome_bin):
#     options = webdriver.ChromeOptions()
#     options.binary_location = chrome_bin
#
#     service = webdriver.ChromeService(executable_path=chromedriver_bin)
#
#     driver = webdriver.Chrome(service=service, options=options)
#
#     driver.quit()
#
#
# def test_driver_port():
#     service = webdriver.ChromeService(port=1234)
#
#     driver = webdriver.Chrome(service=service)

    driver.quit()