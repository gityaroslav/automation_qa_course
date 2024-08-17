from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        actions = ActionChains(self.driver)
        actions.double_click(element)
        actions.perform()

    def action_right_click(self, element):
        actions = ActionChains(self.driver)
        actions.context_click(element)
        actions.perform()

    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def switch_to_frame(self, index):
        self.driver.switch_to.frame(index)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def go_to_visible_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        self.go_to_element(element)  # Прокручуємо до елемента
        return element

    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def select_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

    def actions_drag_and_drop_by_offset(self, element, x, y):
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(element, x, y)
        actions.perform()





