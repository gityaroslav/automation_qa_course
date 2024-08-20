from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators
from pages.base_page import BasePage
import random


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def change_list_order(self):
        return self.change_elements_order(self.locators.TAB_LIST, self.locators.LIST_ITEM)

    def change_greed_order(self):
        return self.change_elements_order(self.locators.TAB_GREED, self.locators.GREED_ITEM)


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def select_list_items(self):
        self.go_to_visible_element(self.locators.TAB_LIST).click()
        random_elements = self.random_elements_from_list(self.locators.LIST_ITEM)
        self.actions_click_selected_elements(random_elements)
        return self.check_selected_items(random_elements)

    def check_selected_list_items(self):
        return self.check_selected_items(self.elements_are_present(self.locators.LIST_RESULT))

    def select_greed_items(self):
        self.go_to_visible_element(self.locators.TAB_GREED).click()
        random_elements = self.random_elements_from_list(self.locators.GREED_ITEM)
        self.actions_click_selected_elements(random_elements)
        return self.check_selected_items(random_elements)

    def check_selected_greed_items(self):
        return self.check_selected_items(self.elements_are_present(self.locators.GREED_RESULT))

