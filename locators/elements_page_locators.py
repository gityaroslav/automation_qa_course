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


class WebTablePageLocators:
    #add person form
    ADD_BUTTON = (By.ID, 'addNewRecordButton')
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="firstName"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@id="lastName"]')
    EMAIL_INPUT = (By.XPATH, '//input[@id="userEmail"]')
    AGE_INPUT = (By.XPATH, '//input[@id="age"]')
    SALARY_INPUT = (By.XPATH, '//input[@id="salary"]')
    DEPARTMENT_INPUT = (By.XPATH, '//input[@id="department"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submit"]')

    #tables
    FULL_PEOPLE_LIST = (By.XPATH, '//div[@class="rt-tr-group"]')
    SEARCH_INPUT = (By.XPATH, '//input[@id="searchBox"]')
    DELETE_BUTTON = (By.XPATH, '//span[@title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'

