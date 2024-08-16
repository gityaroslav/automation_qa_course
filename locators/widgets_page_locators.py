from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_SECTION = (By.XPATH, '//div[@id="section1Heading"]')
    SECOND_SECTION = (By.XPATH, '//div[@id="section2Heading"]')
    THIRD_SECTION = (By.XPATH, '//div[@id="section3Heading"]')

    FIRST_CONTENT = (By.XPATH, '//div[@id="section1Content"]//p')
    SECOND_CONTENT = (By.XPATH, '//div[@id="section2Content"]//p')
    THIRD_CONTENT = (By.XPATH, '//div[@id="section3Content"]//p')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.XPATH, '//input[@id="autoCompleteMultipleInput"]')
    SELECTED_COLORS = (By.XPATH, '//div[@class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    REMOVE_COLORS = (By.XPATH, '//div[contains(@class, "auto-complete__multi-value__remove")]')
    REMOVE_ALL = (By.XPATH, "//div[contains(@class, 'auto-complete__clear-indicator')]")

    SINGLE_INPUT = (By.XPATH, '//input[@id="autoCompleteSingleInput"]')
    SELECTED_COLOR = (By.XPATH, '//div[contains(@class, "css-1uccc91-singleValue")]')