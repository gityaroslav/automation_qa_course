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


class ResizablePageLocators:
    TITLE = (By.XPATH, '//h1[text()="Resizable"]')
    RESIZEABLE_BOX = (By.XPATH, '//div[@id="resizableBoxWithRestriction"]')
    RESIZEABLE_BOX_HANDLE = (By.XPATH, '//div[@id="resizableBoxWithRestriction"]/span')
    RESIZEABLE = (By.XPATH, '//div[@id="resizable"]')
    RESIZEABLE_HANDLE = (By.XPATH, '//div[@id="resizable"]/span')


class DroppablePageLocators:
    # Simple
    SIMPLE_TAB = (By.XPATH, '//a[@id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.XPATH, '//div[@id="draggable"]')
    DROP_ME_SIMPLE = (By.XPATH, '//div[@id="simpleDropContainer"]//div[@id="droppable"]')
    # Accept
    ACCEPT_TAB = (By.XPATH, '//a[@id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.XPATH, '//div[@id="acceptable"]')
    NOT_ACCEPTABLE = (By.XPATH, '//div[@id="notAcceptable"]')
    DROP_ME_ACCEPT = (By.XPATH, '//div[@id="acceptDropContainer"]//div[@id="droppable"]')
    # Prevent Propogation
    PREVENT_TAB = (By.XPATH, '//a[@id="droppableExample-tab-preventPropogation"]')
    DRAG_ME_PREVENT = (By.XPATH, '//div[@id="dragBox"]')
    OUTER_NOT_GREEDY = (By.XPATH, '//div[@id="notGreedyDropBox"]')
    INNER_NOT_GREEDY = (By.XPATH, '//div[@id="notGreedyDropBox"]//div[@id="notGreedyInnerDropBox"]')
    OUTER_GREEDY = (By.XPATH, '//div[@id="greedyDropBox"]')
    INNER_GREEDY = (By.XPATH, '//div[@id="greedyDropBox"]//div[@id="greedyDropBoxInner"]')
    # Revert Draggable
    REVERT_TAB = (By.XPATH, '//a[@id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.XPATH, '//div[@id="revertable"]')
    NOT_REVERT = (By.XPATH, '//div[@id="notRevertable"]')
    DROP_ME_REVERT = (By.XPATH, '//div[@id="revertableDropContainer"]//div[@id="droppable"]')