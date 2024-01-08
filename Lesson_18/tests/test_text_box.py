from Hillel_Course_AQA_Podlinnov.Lesson_18.TextBoxPage_my import TextBoxPage


class TestTextBox:

    def test_text_box(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Andrii")
        page.fill_full_email_field("Andrii@email.com")
        page.fill_full_current_text_area_field("Hello, this is Ololo!1")
        page.fill_full_permanent_text_area_field("Andrii, some text permanent")
        page.scroll_down()
        page.click_submit()

    def test_chek_fill_full_name(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Andrii")
        page.scroll_down()
        name_field = page.get_result_fullname()
        page.click_submit()
        assert name_field.replace("Name:") == "Andrii"
        # assert name_field.split(":")[1] == "Andrii"

