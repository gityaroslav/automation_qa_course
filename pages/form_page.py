import os
import time
import random

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_all_form_fields(self):
        person_info = next(generated_person())
        file_name, path = generated_file()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person_info.first_name)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person_info.last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person_info.email)
        # select random gender
        gender_list = self.elements_are_visible(self.locators.ALL_GENDER_INPUT)
        gender = random.choice(gender_list)
        self.go_to_element(gender)
        gender.click()
        # random phone input
        self.element_is_visible(self.locators.MOBILE_NUMBER_INPUT).send_keys(person_info.mobile)
        # random date of birth input
        date_ofb = self.element_is_visible(self.locators.DATE_OF_BIRTH_INPUT)
        date_ofb.click()
        date_ofb.send_keys(Keys.CONTROL + "a")
        date_ofb.send_keys(person_info.date_of_birth)
        date_ofb.send_keys(Keys.ENTER)
        # select random subjects
        subjects = [
            "Hindi", "English", "Maths", "Physics", "Chemistry",
            "Biology", "Computer Science", "Commerce", "Accounting",
            "Economics", "Arts", "Social Studies", "History", "Civics"
            ]
        random_count = random.randint(1, len(subjects))
        random_subjects = random.sample(subjects, random_count)
        for subject in random_subjects:
            subject_input = self.element_is_visible(self.locators.SUBJECTS_INPUT)
            subject_input.send_keys(subject[:3])
            subject_input.send_keys(Keys.ENTER)
        # select random hobbies
        hobbies_list = self.elements_are_visible(self.locators.ALL_HOBBY_INPUT)
        random_hobbies_count = random.randint(1, len(hobbies_list))
        random_checkboxes = random.sample(hobbies_list, random_hobbies_count)
        for checkbox in random_checkboxes:
            checkbox.click()
        # upload file
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        # random address input
        self.element_is_visible(self.locators.CURRENT_ADDRESS_INPUT).send_keys(person_info.current_address)
        # select random state and city and click submit button
        states = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
        state = random.choice(states)
        state_input = self.element_is_visible(self.locators.SELECT_STATE)
        self.go_to_element(state_input)
        state_input.click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(state)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return person_info

    def form_result(self):
        result_list = self.elements_are_present(self.locators.TABLE_RESULT)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data

