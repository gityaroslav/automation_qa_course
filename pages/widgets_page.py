from locators.widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, num):
        if num == "first":
            title_text = self.element_is_visible(self.locators.FIRST_SECTION).text
            content = self.element_is_visible(self.locators.FIRST_CONTENT).text
            # return [title_text, len(content)]
        if num == "second":
            title = self.element_is_visible(self.locators.SECOND_SECTION)
            self.go_to_element(title)
            title.click()
            title_text = title.text
            content = self.element_is_visible(self.locators.SECOND_CONTENT).text
        if num == "third":
            title = self.element_is_visible(self.locators.THIRD_SECTION)
            self.go_to_element(title)
            title.click()
            title_text = title.text
            content = self.element_is_visible(self.locators.THIRD_CONTENT).text
        return [title_text, len(content)]


