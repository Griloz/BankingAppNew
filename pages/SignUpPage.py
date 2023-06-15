from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.BasePage import BasePage
from logs.logger import logger
from configs import config
from faker import Faker
from random import choice
import random
from selenium.webdriver.common.action_chains import ActionChains


class SignUpPage(BasePage):

    def Sign_Up(self):
        # Find and click the sign-up link
        sign_up_link = self.driver.find_element(
            By.CLASS_NAME, "sign-up__content__link").click()


class FakeAccount(SignUpPage):
    # Class attributes
    First_Name = (By.CSS_SELECTOR, "#first-n-input")
    Last_Name = (By.CSS_SELECTOR, '#last-name-input')
    Username = (By.CSS_SELECTOR, '#username')
    Email = (By.CSS_SELECTOR, '#em')
    Confirm_email = (By.CSS_SELECTOR, '#confirm-em')
    Password = (By.CSS_SELECTOR, '#no-autocomplete')
    Confirm_password = (By.CSS_SELECTOR, '#confirm-ps')
    Answer = (By.CSS_SELECTOR, '#securityQuestionAnswer')

    def create_account(self, email, password):
        fake = Faker()
        # Fill in the account creation form
        self.driver.find_element(*self.First_Name).send_keys(fake.first_name())
        self.driver.find_element(*self.Last_Name).send_keys(fake.last_name())
        self.driver.find_element(*self.Username).send_keys(fake.user_name())
        self.driver.find_element(*self.Email).send_keys(email)
        self.driver.find_element(*self.Confirm_email).send_keys(email)
        self.driver.find_element(*self.Password).send_keys(password)
        self.driver.find_element(*self.Confirm_password).send_keys(password)
        # self.randomly_Security_question()
        self.driver.find_element(*self.Answer).send_keys(fake.word())

        # Scroll the page to the checkbox element
        checkbox = self.driver.find_element(
            By.CSS_SELECTOR, '.checkbox-checkmark')
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", checkbox)

        # Click the checkbox element
        self.driver.execute_script("arguments[0].click();", checkbox)

        # Click the second "Sign Up" button (registration confirmation)
        sign_up_button_2 = self.driver.find_element(
            By.XPATH, "//div[2]/app-signup/div/form/div[4]/button")
        sign_up_button_2.click()

    def randomly_Security_question(self):
        options = self.driver.find_elements(
            By.CSS_SELECTOR, '#securityQuestionId')
        options[0].click()
        element = self.driver.find_element(
            By.XPATH, "//span[text()='Your city of birth?']")
        element.click()
