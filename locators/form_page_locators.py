from selenium.webdriver.common.by import By


class FormPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, '//input[@id="firstName"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@id="lastName"]')
    EMAIL_INPUT = (By.XPATH, '//input[@id="userEmail"]')
    ALL_GENDER_INPUT = (By.XPATH, '//div[@class="custom-control custom-radio custom-control-inline"]')
    MOBILE_NUMBER_INPUT = (By.XPATH, '//input[@id="userNumber"]')
    DATE_OF_BIRTH_INPUT = (By.XPATH, '//input[@id="dateOfBirthInput"]')
    SUBJECTS_INPUT = (By.XPATH, '//input[@id="subjectsInput"]')
    ALL_HOBBY_INPUT = (By.XPATH, '//div[@class="custom-control custom-checkbox custom-control-inline"]')
    FILE_INPUT = (By.XPATH, '//input[@id="uploadPicture"]')
    CURRENT_ADDRESS_INPUT = (By.XPATH, '//textarea[@id="currentAddress"]')
    SELECT_STATE = (By.XPATH, '//*[@id="state"]/div/div[1]')
    STATE_INPUT = (By.XPATH, '//input[@id="react-select-3-input"]')
    SELECT_CITY = (By.XPATH, '//*[@id="city"]/div/div[1]/div[1]')
    CITY_INPUT = (By.XPATH, '//input[@id="react-select-4-input"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submit"]')

    #table result
    TABLE_RESULT = (By.XPATH, '//div[@class="table-responsive"]//td[2]')