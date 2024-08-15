import time
import random
from locators.alerts_frame_windows_locators import BrowserWindowsLocators, AlertsPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsLocators()

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


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alerts(self):
        self.element_is_visible(self.locators.ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        return alert_window.text
        alert_window.accept()

    def check_see_alerts_after(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        time.sleep(5)
        alert_window = self.switch_to_alert()
        return alert_window.text
        alert_window.accept()

    def check_confirm_box(self, confirm=True):
        button = self.element_is_visible(self.locators.CONFIRM_BUTTON)
        self.go_to_element(button)
        button.click()
        alert_window = self.switch_to_alert()
        if confirm:
            alert_window.accept()
        else:
            alert_window.dismiss()
        text = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text

    def check_prompt_box(self):
        info = next(generated_person())
        prompt_box = self.element_is_visible(self.locators.PROMPT_BUTTON)
        self.go_to_element(prompt_box)
        prompt_box.click()
        alert_window = self.switch_to_alert()
        alert_window.send_keys(info.first_name)
        alert_window.accept()
        text = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, info.first_name

