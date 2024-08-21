from locators.elements_page_locators import ResizablePageLocators
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


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizeable_box(self):
        self.actions_drag_and_drop_by_offset(self.go_to_visible_element(
            self.locators.RESIZEABLE_BOX_HANDLE), 310, 110)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZEABLE_BOX))
        title = self.element_is_present(self.locators.TITLE)
        self.go_to_element(title)
        self.actions_drag_and_drop_by_offset(self.element_is_present(
            self.locators.RESIZEABLE_BOX_HANDLE), -360, -160)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZEABLE_BOX))
        return max_size, min_size

    def change_size_resizeable(self):
        self.actions_drag_and_drop_by_offset(self.go_to_visible_element(self.locators.RESIZEABLE_HANDLE),
                                             random.randint(1, 150), random.randint(1, 150))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZEABLE))
        self.actions_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZEABLE_HANDLE),
                                             random.randint(-150, -1), random.randint(-150, -1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZEABLE))
        return max_size, min_size
