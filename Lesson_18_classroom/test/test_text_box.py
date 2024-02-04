from Hillel_Course_AQA_Podlinnov.Lesson_18_classroom.TextBoxPage import TextBoxPage


class TestTextBox:

    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Pavlo")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Pavlo"

    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_email_field("andrii@gmail.com")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_email()
        assert name_field.replace("Email:", "") == "andrii@gmail.com"

    def test_curr_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_current_address_field("Ukraine, Kiyv, Maidan Nezalezhnosti 1")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_current_address()
        assert name_field.replace("Current Address :", "") == "Ukraine, Kiyv, Maidan Nezalezhnosti 1"

    def test_perm_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_permanent_address_field("Адреса українською")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_permanent_address()
        assert name_field.replace("Permananet Address :", "") == "Адреса українською"
