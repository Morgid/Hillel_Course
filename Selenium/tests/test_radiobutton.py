from selenium.webdriver.common.by import By

from Hillel_Course_AQA_Podlinnov.Selenium.RadioButtonPage import RadioButton


# Написати тести: на сторінці https://demoqa.com/radio-button А)(test_activate_yes_radio)
# Активувати кнопку Yes та переконатись що вона активована. Переконатись двома різними способами.
# Б)(test_get_radio_buttons_info) Визначити які є радіо-баттони на сторінці та
# сформувати словник із такими даними: Назва кнопки, Чи увімкнена кнопка, Чи активна (обрана) кнопка. В


# def test_radio(chrome):
#     chrome.get("https://demoqa.com/radio-button")
#     ra_yes = RadioButton(driver=chrome, locator=(By.XPATH, "//label[.='{}']//ancestor::div[contains(@class, 'radio')]"), name="Yes")
#     ra_yes.select()
#     print('Ololo')

def test_activate_yes_radio(chrome):
    chrome.get("https://demoqa.com/radio-button")
    radio_activate_yes = RadioButton(driver=chrome,
                                     locator=(By.XPATH, "//label[normalize-space(.)='Yes']//ancestor::div[contains(@class, 'radio')]"),
                                     name='Yes')
    radio_activate_yes.select()
    text_confirm_locator = chrome.find_element(By.XPATH, '//label[@class="text-success"]')
    assert text_confirm_locator.text == "Impressive"
    assert text_confirm_locator.is_displayed()
