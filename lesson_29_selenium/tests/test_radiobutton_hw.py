from selenium.webdriver.common.by import By

from lesson_29_selenium.RadioButtonPage import RadioButton


def test_radio(chrome):
    chrome.get("https://demoqa.com/radio-button")
    ra_yes = RadioButton(driver=chrome, locator=(By.XPATH, "//label[.='{}']//ancestor::div[contains(@class, 'radio')]"),
                         name="Impressive")
    ra_yes.select()


def test_activate_yes_radio(chrome):
    chrome.get("https://demoqa.com/radio-button")
    ra_yes = RadioButton(driver=chrome, locator=(By.XPATH, "//label[.='{}']"), name="Yes")
    ra_yes.select()
    locator_sucsess = chrome.find_element(By.XPATH, '//*[@class="text-success"]')
    assert locator_sucsess.is_enabled()
    assert locator_sucsess.text == "Yes"


def test_get_radio_buttons_info(chrome):
    chrome.get("https://demoqa.com/radio-button")
    radio_buttons = chrome.find_elements(By.XPATH, '//*[@type="radio"]')
    radio_buttons_info = {}
    for button in radio_buttons:
        button_name = button.find_element(By.XPATH, "./../label").text
        button_enable = button.is_enabled()
        if button_enable == True:
            button_enable = 'Так'
        else:
            button_enable = 'Ні'
        button_selected = button.is_selected()
        if button_selected == True:
            button_selected = 'Так'
        else:
            button_selected = 'Ні'
        radio_buttons_info[f'Кнопка {button_name}'] = {'Чи увімкнена кнопка': button_enable,
                                                       "Чи активна (обрана) кнопка": button_selected}
    for button_name, button_info in radio_buttons_info.items():
        print(button_name)
        print(f"Чи увімкнена кнопка: {button_info['Чи увімкнена кнопка']}")
        print(f"Чи активна (обрана) кнопка: {button_info['Чи активна (обрана) кнопка']}")
        print()
