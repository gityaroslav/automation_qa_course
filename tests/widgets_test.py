from pages.widgets_page import AccordianPage


class TestWidgets:
    class TestAccordianPage:
        def test_first_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            result = accordian_page.check_accordian("first")
            assert result == ['What is Lorem Ipsum?', 574]

        def test_second_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            result = accordian_page.check_accordian("second")
            assert result == ['Where does it come from?', 763]

        def test_third_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            result = accordian_page.check_accordian("third")
            assert result == ['Why do we use it?', 613]

        def test_all_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            result1 = accordian_page.check_accordian("first")
            result2 = accordian_page.check_accordian("second")
            result3 = accordian_page.check_accordian("third")
            assert result1 == ['What is Lorem Ipsum?', 574]
            assert result2 == ['Where does it come from?', 763]
            assert result3 == ['Why do we use it?', 613]

