from locators.widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, num):
        if num == "first":
            title_text = self.go_to_visible_element(self.locators.FIRST_SECTION).text
            content = self.go_to_visible_element(self.locators.FIRST_CONTENT).text
        if num == "second":
            self.go_to_visible_element(self.locators.SECOND_SECTION).click()
            title_text = self.go_to_visible_element(self.locators.SECOND_SECTION).text
            content = self.element_is_visible(self.locators.SECOND_CONTENT).text
        if num == "third":
            self.go_to_visible_element(self.locators.THIRD_SECTION).click()
            title_text = self.go_to_visible_element(self.locators.THIRD_SECTION).text
            content = self.element_is_visible(self.locators.THIRD_CONTENT).text
        return [title_text, len(content)]


