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


class DatePickerPageLocators:
    DATE_INPUT = (By.XPATH, '//input[@id="datePickerMonthYearInput"]')
    DATE_SELECT_DAY_LIST = (By.XPATH, '//div[contains(@class, "react-datepicker__day react-datepicker")]')
    DATE_SELECT_MONTH = (By.XPATH, '//select[@class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.XPATH, '//select[@class="react-datepicker__year-select"]')

    DATE_TIME_INPUT = (By.XPATH, '//input[@id="dateAndTimePickerInput"]')
    DATE_TIME_DAY_LIST = (By.XPATH, '//div[contains(@class, "react-datepicker__day react-datepicker__day") and not('
                                    'contains(@class, "react-datepicker__day--outside-month"))]')
    DATE_TIME_MONTH = (By.XPATH, '//span[@class="react-datepicker__month-read-view--down-arrow"]')
    DATE_TIME_MONTH_LIST = (By.XPATH, '//div[contains(@class, "react-datepicker__month-option")]')
    DATE_TIME_YEAR = (By.XPATH, '//span[@class="react-datepicker__year-read-view--selected-year"]')
    DATE_TIME_YEAR_LIST = (By.XPATH, '//div[contains(@class, "react-datepicker__year-option")]')
    DATE_TIME_TIME_LIST = (By.XPATH, '//li[@class="react-datepicker__time-list-item "]')