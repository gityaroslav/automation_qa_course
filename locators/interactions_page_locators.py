from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.XPATH, '//a[@id="demo-tab-list"]')
    LIST_ITEM = (By.XPATH, '//div[@class="vertical-list-container mt-4"]/div')
    TAB_GREED = (By.XPATH, '//a[@id="demo-tab-grid"]')
    GREED_ITEM = (By.XPATH, '//div[@class="create-grid"]/div')


class SelectablePageLocators:
    TAB_LIST = (By.XPATH, '//a[@id="demo-tab-list"]')
    LIST_ITEM = (By.XPATH, '//ul[@id="verticalListContainer"]/li')
    LIST_RESULT = (By.XPATH, '//ul[@id="verticalListContainer"]//li[contains(@class, "active")]')
    TAB_GREED = (By.XPATH, '//a[@id="demo-tab-grid"]')
    GREED_ITEM = (By.XPATH, '//div[@id="gridContainer"]//li')
    GREED_RESULT = (By.XPATH, '//div[@id="gridContainer"]//li[contains(@class, "active")]')