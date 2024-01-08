from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class TextBoxPage:
    def __init__(self, driver: WebDriver):
        self.url = "https://demoqa.com/text-box"
        self.driver = driver
        self.full_name_field = (By.ID, "userName")
        # self.full_name_field = (By.XPATH, "//input[@id='userName']") # доступ до юзернейма через Хпас та інпут
        self.full_email_field = (By.ID, "userEmail")
        self.full_current_text_area_field = (By.ID, "currentAddress")
        # self.full_permanent_address = (By.ID, "permanentAddress") - тут через айді
        self.full_permanent_text_area_field = (By.CSS_SELECTOR, "textarea#permanentAddress")
        self.submit_btn = (By.ID, "submit") # кнопка пишеться зазвичай як btn

    def open(self) -> "TextBoxPage":
        self.driver.get(self.url)
        return self

    def clear_full_name_field(self) -> None: #чистимо поле
        self.driver.find_element(*self.full_name_field).clear()

    def fill_full_name_field(self, text: str) -> None : #додаємо в поле текст, наповнення
        self.driver.find_element(*self.full_name_field).send_keys(text)


# Домашка))
    # def clear_full_email_field(self) -> None:  # чистимо поле
    #     self.driver.find_element(*self.full_email_field).clear()
    #
    # def fill_full_email_field(self, text: str) -> None:  # додаємо в поле текст, наповнення
    #     self.driver.find_element(*self.full_email_field).send_keys(text)

    # def clear_full_current_text_area_field(self) -> None:  # чистимо поле
    #     self.driver.find_element(*self.full_current_text_area_field).clear()
    #
    # def fill_full_current_text_area_field(self, text: str) -> None:  # додаємо в поле текст, наповнення
    #     self.driver.find_element(*self.full_current_text_area_field).send_keys(text)

    # def clear_full_permanent_text_area_field(self) -> None:  # чистимо поле
    #     self.driver.find_element(*self.full_permanent_text_area_field).clear()
    #
    # def fill_full_permanent_text_area_field(self, text: str) -> None:  # додаємо в поле текст, наповнення
    #     self.driver.find_element(*self.full_permanent_text_area_field).send_keys(text)
# Done Домашка, перепровірить

    # на домашку повторити методи по два для Чистимо поле та наповрення для емайла та каррент адресси, ну і мабуть для перманент текста

    def click_submit(self) -> None:
        self.driver.find_element(*self.submit_btn).click()
