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


class SliderPageLocators:
    SLIDER_INPUT = (By.XPATH, '//input[@class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.XPATH, '//input[@id="sliderValue"]')


class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.XPATH, '//button[@id="startStopButton"]')
    PROGRESS_BAR_VALUE = (By.XPATH, '//div[@class="progress-bar bg-info"]')


class TabsPageLocators:
    TABS_WHAT = (By.XPATH, '//a[@id="demo-tab-what"]')
    TABS_WHAT_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-what"]//p')
    TABS_ORIGIN = (By.XPATH, '//a[@id="demo-tab-origin"]')
    TABS_ORIGIN_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-origin"]//p')
    TABS_USE = (By.XPATH, '//a[@id="demo-tab-use"]')
    TABS_USE_CONTENT = (By.XPATH, '//div[@id="demo-tabpane-use"]//p')
    TABS_MORE = (By.XPATH, '//a[@id="demo-tab-more"]')


class ToolTipsPageLocators:
    BUTTON = (By.XPATH, '//button[@id="toolTipButton"]')
    TOOLTIP_BUTTON = (By.XPATH, '//button[@aria-describedby="buttonToolTip"]')
    FIELD = (By.XPATH, '//input[@id="toolTipTextField"]')
    TOOLTIP_FIELD = (By.XPATH, '//input[@aria-describedby="textFieldToolTip"]')
    CONTRARY_LINK = (By.XPATH, '//div[@id="texToolTopContainer"]//a[text()="Contrary"]')
    TOOLTIP_CONTRARY = (By.XPATH, '//a[@aria-describedby="contraryTexToolTip"]')
    SECTION_LINK = (By.XPATH, '//div[@id="texToolTopContainer"]//a[text()="1.10.32"]')
    TOOLTIP_SECTION = (By.XPATH, '//a[@aria-describedby="sectionToolTip"]')
    RESULT = (By.XPATH, '//div[@class="tooltip-inner"]')


class MenuPageLocators:
    MENU_ITEM_LIST = (By.XPATH, '//ul[@id="nav"]//a')


class SelectMenuPageLocators:
    SELECT_VALUE = (By.XPATH, '(//div[@class=" css-tlfecz-indicatorContainer"])[1]')
    VALUE_INPUT = (By.XPATH, '//input[@id="react-select-2-input"]')
    SELECT_VALUE_RESULT = (By.XPATH, '//div[@id="withOptGroup"]//div[contains(@class, "singleValue")]')
    SELECT_ONE = (By.XPATH, '//input[@id="react-select-3-input"]')
    SELECT_ONE_RESULT = (By.XPATH, '//div[@id="selectOne"]//div[@class=" css-1uccc91-singleValue"]')
    OLD_SELECT = (By.XPATH, '//select[@id="oldSelectMenu"]')
    MULTI_DROP_DOWN = (By.XPATH, '//input[@id="react-select-4-input"]')
    MULTI_RESULT_LIST = (By.XPATH, '//div[@class="css-12jo7m5"]')
    CARS_SELECT = (By.XPATH, '//select[@id="cars"]')


