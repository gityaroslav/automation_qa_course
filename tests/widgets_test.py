from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage


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

    class TestAutoComplete:
        def test_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            selected_colors = autocomplete_page.check_multiple_autocomplete()
            colors_result = autocomplete_page.check_selected_colors()
            assert selected_colors == colors_result, 'colors has been selected incorrectly'

        def test_multi_remove(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.check_multiple_autocomplete()
            colors_result = autocomplete_page.check_selected_colors()
            colors_after = autocomplete_page.remove_color()
            assert len(colors_result) > len(colors_after), 'colors has not been removed correctly'

        def test_multi_remove_all(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.check_multiple_autocomplete()
            autocomplete_page.remove_all()
            result = autocomplete_page.check_selected_colors()
            assert result == 'no colors were found', "colors has been removed incorrectly"

        def test_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            input_color = autocomplete_page.fill_single_color()
            output_color = autocomplete_page.check_single_color()
            assert input_color == output_color, 'colors has not match'

        def test_date_picker(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            before, after = date_picker_page.select_random_date()
            assert before != after, 'the date has not been changed'

        def test_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            before, after = date_picker_page.set_random_date_time()
            assert before != after, 'the date has not been changed'

        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            before, after = slider_page.change_slider_value()
            assert before != after, 'the slider has not been changed'

        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            value = progress_bar_page.change_progress_bar_value()
            assert value > "0", 'progress bar has not been changed'

        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            what_tab = tabs_page.check_tabs('what')
            origin_tab = tabs_page.check_tabs('origin')
            use_tab = tabs_page.check_tabs('use')
            more_tab = tabs_page.check_tabs('more')
            assert what_tab == ['What', 574], 'the tab "what" has not been selected'
            assert origin_tab == ['Origin', 763], 'the tab "origin" has not been selected'
            assert use_tab == ['Use', 613], 'the tab "use" has not been selected'
            assert more_tab == ['More', 0], 'the tab "more" has not been selected'


