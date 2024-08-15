from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_SECTION = (By.XPATH, '//div[@id="section1Heading"]')
    SECOND_SECTION = (By.XPATH, '//div[@id="section2Heading"]')
    THIRD_SECTION = (By.XPATH, '//div[@id="section3Heading"]')

    FIRST_CONTENT = (By.XPATH, '//div[@id="section1Content"]//p')
    SECOND_CONTENT = (By.XPATH, '//div[@id="section2Content"]//p')
    THIRD_CONTENT = (By.XPATH, '//div[@id="section3Content"]//p')