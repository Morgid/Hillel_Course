from selenium.webdriver.common.by import By

from Hillel_Course_AQA_Podlinnov.Selenium.RadioButtonPage import RadioButton


def test_activate_yes_radio(chrome):
    chrome.get("https://demoqa.com/radio-button")
    radio_activate_yes = RadioButton(driver=chrome,
                                     locator=(By.XPATH, "//label[normalize-space(.)='Yes']//ancestor::div[contains(@class, 'radio')]"),
                                     name='Impressive')
