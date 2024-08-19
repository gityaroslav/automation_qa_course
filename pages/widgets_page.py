import random
import time
from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, num):
        if num == "first":
            title_text = self.go_to_visible_element(self.locators.FIRST_SECTION).text
            content = self.go_to_visible_element(self.locators.FIRST_CONTENT).text
        elif num == "second":
            self.go_to_visible_element(self.locators.SECOND_SECTION).click()
            title_text = self.go_to_visible_element(self.locators.SECOND_SECTION).text
            content = self.element_is_visible(self.locators.SECOND_CONTENT).text
        elif num == "third":
            self.go_to_visible_element(self.locators.THIRD_SECTION).click()
            title_text = self.go_to_visible_element(self.locators.THIRD_SECTION).text
            content = self.element_is_visible(self.locators.THIRD_CONTENT).text
        else:
            raise ValueError("Invalid 'num' value. Please use 'first', 'second', or 'third'.")
        return [title_text, len(content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def check_multiple_autocomplete(self):
        colors = next(generated_color()).color_name
        random_count = random.randint(2, len(colors))
        random_colors = random.sample(colors, random_count)
        data = []
        for color in random_colors:
            multi_input = self.go_to_visible_element(self.locators.MULTI_INPUT)
            multi_input.send_keys(color[:3])
            multi_input.send_keys(Keys.RETURN)
            data.append(color)
        return data

    def check_selected_colors(self):
        colors = []
        try:
            selected_colors = self.elements_are_present(self.locators.SELECTED_COLORS)
            for item in selected_colors:
                colors.append(item.text)
            return colors
        except TimeoutException:
            return "no colors were found"

    def remove_color(self):
        colors = []
        remove_list = self.elements_are_visible(self.locators.REMOVE_COLORS)
        num_to_remove = random.randint(1, (len(remove_list) - 1))
        elements_to_remove = random.sample(remove_list, num_to_remove)
        for element in elements_to_remove:
            element.click()
        selected_colors = self.elements_are_present(self.locators.SELECTED_COLORS)
        for item in selected_colors:
            colors.append(item.text)
        return colors

    def remove_all(self):
        self.element_is_visible(self.locators.REMOVE_ALL).click()

    def fill_single_color(self):
        colors = next(generated_color()).color_name
        color = random.choice(colors)
        single_input = self.go_to_visible_element(self.locators.SINGLE_INPUT)
        single_input.send_keys(color)
        single_input.send_keys(Keys.RETURN)
        return color

    def check_single_color(self):
        selected_color = self.element_is_visible(self.locators.SELECTED_COLOR)
        return selected_color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_random_date(self):
        date = next(generated_date())
        input_date = self.go_to_visible_element(self.locators.DATE_INPUT)
        date_value_before = input_date.get_attribute('value')
        input_date.click()
        input_date.clear()
        self.select_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.select_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.select_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        date_value_after = input_date.get_attribute('value')
        return date_value_before, date_value_after

    def set_random_date_time(self):
        date = next(generated_date())
        input_date = self.go_to_visible_element(self.locators.DATE_TIME_INPUT)
        date_value_before = input_date.get_attribute('value')
        input_date.click()
        input_date.clear()
        self.element_is_visible(self.locators.DATE_TIME_MONTH).click()
        self.select_date_item_from_list(self.locators.DATE_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_TIME_YEAR).click()
        self.select_date_item_from_list(self.locators.DATE_TIME_YEAR_LIST, date.year_between)
        self.select_date_item_from_list(self.locators.DATE_TIME_DAY_LIST, date.day)
        self.select_date_item_from_list(self.locators.DATE_TIME_TIME_LIST, date.time)
        input_date = self.go_to_visible_element(self.locators.DATE_TIME_INPUT)
        date_value_after = input_date.get_attribute('value')
        return date_value_before, date_value_after


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        slider_value = self.go_to_visible_element(self.locators.SLIDER_VALUE)
        slider_value_before = slider_value.get_attribute('value')
        slider_input = self.go_to_visible_element(self.locators.SLIDER_INPUT)
        self.actions_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        slider_value_after = slider_value.get_attribute('value')
        return slider_value_before, slider_value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        progress_bar_button = self.go_to_visible_element(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 7))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, tab_name):
        content = ''
        if tab_name == "what":
            title = self.go_to_visible_element(self.locators.TABS_WHAT).text
            content = self.element_is_present(self.locators.TABS_WHAT_CONTENT).text
        elif tab_name == "origin":
            self.go_to_visible_element(self.locators.TABS_ORIGIN).click()
            title = self.go_to_visible_element(self.locators.TABS_ORIGIN).text
            content = self.element_is_visible(self.locators.TABS_ORIGIN_CONTENT).text
        elif tab_name == "use":
            self.go_to_visible_element(self.locators.TABS_USE).click()
            title = self.go_to_visible_element(self.locators.TABS_USE).text
            content = self.element_is_visible(self.locators.TABS_USE_CONTENT).text
        elif tab_name == "more":
            title = self.element_is_present(self.locators.TABS_MORE).text
        else:
            raise ValueError("Invalid 'num' value. Please use 'first', 'second', or 'third'.")
        return [title, len(content)]


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tips(self, hover_el, wait_el):
        element = self.element_is_present(hover_el)
        self.go_to_element(element)
        self.actions_move_to_element(element)
        self.ensure_element_focused(element)
        self.element_is_visible(wait_el)
        tool_tip_text = self.go_to_visible_element(self.locators.RESULT)
        text = tool_tip_text.text
        return text

    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOLTIP_BUTTON)
        tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOLTIP_FIELD)
        tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK, self.locators.TOOLTIP_CONTRARY)
        tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION_LINK, self.locators.TOOLTIP_SECTION)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section
