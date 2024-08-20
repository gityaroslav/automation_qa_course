import time

from locators.interactions_page_locators import SortablePageLocators
from pages.base_page import BasePage
import random


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def change_list_order(self):
        return self.change_elements_order(self.locators.TAB_LIST, self.locators.LIST_ITEM)

    def change_greed_order(self):
        return self.change_elements_order(self.locators.TAB_GREED, self.locators.GREED_ITEM)



