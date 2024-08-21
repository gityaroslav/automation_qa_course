import time

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
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


class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.go_to_visible_element(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_ME_SIMPLE)
        self.actions_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        acceptable_div = self.go_to_visible_element(self.locators.ACCEPTABLE)
        not_acceptable_div = self.go_to_visible_element(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_ME_ACCEPT)
        self.actions_drag_and_drop_to_element(not_acceptable_div, drop_div)
        text_not_accept = drop_div.text
        self.actions_drag_and_drop_to_element(acceptable_div, drop_div)
        text_accept = drop_div.text
        return text_not_accept, text_accept

    def drop_prevent(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()
        drag_div = self.go_to_visible_element(self.locators.DRAG_ME_PREVENT)
        inner_not_greedy = self.go_to_visible_element(self.locators.INNER_NOT_GREEDY)
        outer_not_greedy = self.go_to_visible_element(self.locators.OUTER_NOT_GREEDY)
        inner_greedy = self.element_is_visible(self.locators.INNER_GREEDY)
        outer_greedy = self.element_is_visible(self.locators.OUTER_GREEDY)
        self.actions_drag_and_drop_to_element(drag_div, inner_not_greedy)
        text_not_greedy = outer_not_greedy.text
        self.actions_drag_and_drop_to_element(drag_div, inner_greedy)
        text_greedy_inner = outer_greedy.text
        self.actions_drag_and_drop_by_offset(drag_div, 50, 90)
        text_greedy_outer = outer_greedy.text
        return text_not_greedy, text_greedy_inner, text_greedy_outer

    # def drop_revert(self, type_drag):
    #     self.element_is_visible(self.locators.REVERT_TAB).click()
    #     revert = self.go_to_visible_element(self.locators.WILL_REVERT)
    #     not_revert = self.go_to_visible_element(self.locators.NOT_REVERT)
    #     drop_div = self.go_to_visible_element(self.locators.DROP_ME_REVERT)
    #     if type_drag == "revert":
    #         self.actions_drag_and_drop_to_element(revert, drop_div)
    #         position_after_move = revert.get_attribute('style')
    #         time.sleep(1)
    #         position_after_revert = revert.get_attribute('style')
    #     if type_drag == "not_revert":
    #         self.actions_drag_and_drop_to_element(not_revert, drop_div)
    #         position_after_move = not_revert.get_attribute('style')
    #         time.sleep(1)
    #         position_after_revert = not_revert.get_attribute('style')
    #     return position_after_move, position_after_revert

    # def drop_revert(self, type_drag):
    #     drags = {
    #         'will_revert': {'revert': self.locators.WILL_REVERT},
    #         'will_not_revert': {'revert': self.locators.NOT_REVERT},
    #     }
    #     self.element_is_visible(self.locators.REVERT_TAB).click()
    #     element = self.go_to_visible_element(drags[type_drag]['revert'])
    #     drop_div = self.go_to_visible_element(self.locators.DROP_ME_REVERT)
    #     self.actions_drag_and_drop_to_element(element, drop_div)
    #     position_after_move = element.get_attribute('style')
    #     time.sleep(2)
    #     position_after_revert = element.get_attribute('style')
    #     return position_after_move, position_after_revert

    def drop_revert(self, type_drag):
        drags = {
            'will_revert': self.locators.WILL_REVERT,
            'will_not_revert': self.locators.NOT_REVERT,
        }
        self.element_is_visible(self.locators.REVERT_TAB).click()
        element = self.go_to_visible_element(drags[type_drag])
        drop_div = self.go_to_visible_element(self.locators.DROP_ME_REVERT)
        self.actions_drag_and_drop_to_element(element, drop_div)
        position_after_move = element.get_attribute('style')
        time.sleep(2)
        position_after_revert = element.get_attribute('style')
        return position_after_move, position_after_revert







