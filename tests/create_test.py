from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

# importing the LoginPage class from LoginPage file
from pages.LoginPage import LoginPage
from pages.SignUpPage import FakeAccount
from pages.SignUpPage import SignUpPage
from faker import Faker
from random import choice
import random


def test_create_account(driver):
    fake = Faker()   # Create an instance of Faker
    sign_up_page = FakeAccount(driver)
    sign_up_page.Sign_Up()
    sleep(2)  # Added a pause after clicking the first "Sign Up" button
    email = fake.email()
    password = fake.password()
    # Call the randomly_Security_question method
    sign_up_page.randomly_Security_question()
    sign_up_page.create_account(email, password)
    sleep(3)
    message = 'A welcome message with further instructions has been sent to your e-mail address.'
    assert message in driver.page_source
