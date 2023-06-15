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

# create test cases


def test_login_page(driver):
    # check if Login text is displayed
    assert driver.find_element(
        By.CSS_SELECTOR, 'div.heading > h1').text == 'Login'


def test_Sign_Up(driver):
    # check if Login text is displayed
    assert driver.find_element(
        By.XPATH, '//div/span/a').text == 'Sign Up'


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


def test_user_login(driver):
    # create an instance/object of LoginPage class
    login_page = LoginPage(driver)
    # call user_login method of the object
    login_page.user_login()
    assert login_page.text_exists('Log Out')


def test_admin_login(driver):
    # create an instance/object of LoginPage class
    login_page = LoginPage(driver)
    # call user_login method of the object
    login_page.admin_login()
    assert login_page.text_exists('Log Out')


# create a list of tuples, which contains test data
invalid_login_parameters = [
    ('', 'test', 'Field is required'),
    ('aa', 'test', 'Should be minimum 4 chars'),
    ('Test', 'Test', 'Wrong username or password'),
    ('Test', '', 'Field is required'),
    ('*&^hj', 'IUH*&(*)', 'Wrong username or password'),
]

# create a parameterized test case


@pytest.mark.parametrize("username, password, checkpoint", invalid_login_parameters)
def test_invalid_login(driver, username, password, checkpoint):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert login_page.text_exists(checkpoint)
