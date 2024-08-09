from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    CREATED_FULL_NAME = (By.XPATH, '//p[@id="name"]')
    CREATED_EMAIL = (By.XPATH, '//p[@id="email"]')
    CREATED_CURRENT_ADDRESS = (By.XPATH, '//p[@id="currentAddress"]')
    CREATED_PERMANENT_ADDRESS = (By.XPATH, '//p[@id="permanentAddress"]')


class CheckboxPageLocators:
    EXPAND_ALL = (By.XPATH, '//button[@title="Expand all"]')
    ITEM_LIST = (By.XPATH, '//span[@class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    # TITLE_ITEM = ".//ancestor::span[@class='rct-title']"
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']//span[@class='rct-title']"
    OUTPUT_RESULT = (By.XPATH, '//span[@class="text-success"]')


class RadioBottomPageLocators:
    YES = (By.XPATH, '//label[@for="yesRadio"]')
    IMPRESSIVE = (By.XPATH, '//label[@for="impressiveRadio"]')
    NO = (By.XPATH, '//label[@for="noRadio"]')
    RADIO_SELECT = (By.XPATH, '//label[@class="custom-control-label"]')
    RADIO_OUTPUT = (By.XPATH, '//span[@class="text-success"]')
