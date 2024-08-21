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


class FramesPageLocators:
    FRAME1 = (By.XPATH, '//iframe[@id="frame1"]')
    FRAME2 = (By.XPATH, '//iframe[@id="frame2"]')
    FRAME_TEXT = (By.XPATH, '//h1[@id="sampleHeading"]')


class NestedFramesPageLocators:
    PARENT_FRAME = (By.XPATH, '//iframe[@id="frame1"]')
    PARENT_TEXT = (By.TAG_NAME, 'body')
    CHILD_FRAME = (By.XPATH, '//iframe[@srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.TAG_NAME, 'p')


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.XPATH, '//button[@id="showSmallModal"]')
    CLOSE_SMALL = (By.XPATH, '//button[@id="closeSmallModal"]')
    SMALL_TEXT = (By.XPATH, '//div[@class="modal-body"]')
    SMALL_TITLE = (By.XPATH, '//div[@id="example-modal-sizes-title-sm"]')

    LARGE_MODAL_BUTTON = (By.XPATH, '//button[@id="showLargeModal"]')
    CLOSE_LARGE = (By.XPATH, '//button[@id="closeLargeModal""]')
    LARGE_TEXT = (By.XPATH, '//div[@class="modal-body"]//p')
    LARGE_TITLE = (By.XPATH, '//div[@id="example-modal-sizes-title-lg"]')

