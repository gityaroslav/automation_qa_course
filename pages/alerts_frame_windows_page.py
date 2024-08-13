from locators.alerts_frame_windows_locators import TestBrowserWindowsLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = TestBrowserWindowsLocators()

    def check_new_window_or_tab(self, type_):
        if type_ == 'tab':
            button_locator = self.locators.NEW_TAB_BUTTON
        elif type_ == 'window':
            button_locator = self.locators.NEW_WINDOW_BUTTON
        else:
            raise ValueError("Invalid type: choose 'tab' or 'window'")
        self.element_is_visible(button_locator).click()
        self.switch_to_last_window()
        title_text = self.element_is_present(self.locators.NEW_T_W_TEXT).text
        return title_text
