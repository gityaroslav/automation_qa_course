from selenium.webdriver.common.by import By


class TestBrowserWindowsLocators:
    NEW_TAB_BUTTON = (By.XPATH, '//button[@id="tabButton"]')
    NEW_T_W_TEXT = (By.XPATH, '//h1[@id="sampleHeading"]')
    NEW_WINDOW_BUTTON = (By.XPATH, '//button[@id="windowButton"]')
