from pages.form_page import FormPage


class TestForm:
    class TestFormPage:
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            per = form_page.fill_all_form_fields()
            result = form_page.form_result()
            assert [result[0], result[1]] == [per.first_name + " " + per.last_name, per.email], ('the form has been '
                                                                                                 'filled incorrect')
