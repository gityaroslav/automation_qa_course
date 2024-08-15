import time
import random
from locators.alerts_frame_windows_locators import BrowserWindowsLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators
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


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_num):
        if frame_num == "frame1":
            frame = self.element_is_present(self.locators.FRAME1)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.switch_to_frame(frame)
            text = self.element_is_present(self.locators.FRAME_TEXT).text
            self.switch_to_default_content()
            return [text, width, height]
        if frame_num == "frame2":
            frame = self.element_is_present(self.locators.FRAME2)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.switch_to_frame(frame)
            text = self.element_is_present(self.locators.FRAME_TEXT).text
            self.switch_to_default_content()
            return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    def check_modal_dialogs(self, size):
        if size == "small":
            small_button = self.element_is_visible(self.locators.SMALL_MODAL_BUTTON)
            self.go_to_element(small_button)
            small_button.click()
            small_title = self.element_is_present(self.locators.SMALL_TITLE).text
            small_text = self.element_is_present(self.locators.SMALL_TEXT).text
            return [small_title, len(small_text)]
        if size == "large":
            large_button = self.element_is_visible(self.locators.LARGE_MODAL_BUTTON)
            self.go_to_element(large_button)
            large_button.click()
            large_title = self.element_is_present(self.locators.LARGE_TITLE).text
            large_text = self.element_is_present(self.locators.LARGE_TEXT).text
            return [large_title, len(large_text)]
