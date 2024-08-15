from selenium.webdriver.common.by import By


class BrowserWindowsLocators:
    NEW_TAB_BUTTON = (By.XPATH, '//button[@id="tabButton"]')
    NEW_T_W_TEXT = (By.XPATH, '//h1[@id="sampleHeading"]')
    NEW_WINDOW_BUTTON = (By.XPATH, '//button[@id="windowButton"]')


class AlertsPageLocators:
    ALERT_BUTTON = (By.XPATH, '//button[@id="alertButton"]')
    TIMER_ALERT_BUTTON = (By.XPATH, '//button[@id="timerAlertButton"]')
    CONFIRM_BUTTON = (By.XPATH, '//button[@id="confirmButton"]')
    CONFIRM_RESULT = (By.XPATH, '//span[@id="confirmResult"]')
    PROMPT_BUTTON = (By.XPATH, '//button[@id="promtButton"]')
    PROMPT_RESULT = (By.XPATH, '//span[@id="promptResult"]')
