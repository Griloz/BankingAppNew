import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.AccountsPage import AccountsPage, AccountsInfo
from logs.logger import logger


expected_info = {
    'EBQ11113487654': {
        'holder_name': 'John Doe',
        'currency': 'EUR',
        'status': 'Active',
        'account_type': 'Checking'
    },
    'EBQ11223487456': {
        'holder_name': 'John Doe',
        'currency': 'EUR',
        'status': 'Active',
        'account_type': 'Savings'
    },
    'EBQ11223387654': {
        'holder_name': 'John Doe',
        'currency': 'EUR',
        'status': 'Active',
        'account_type': 'Savings'
    },
    'EBQ38495629375': {
        'holder_name': 'John Doe',
        'currency': 'USD',
        'status': 'Active',
        'account_type': 'Checking'
    },
    '511264340': {
        'holder_name': 'John Doe',
        'currency': 'BTC',
        'status': 'Active',
        'account_type': 'BTC Wallet'
    }
}


@pytest.mark.parametrize("account_number", expected_info)
def test_account_info(driver, account_number):
    # Create an instance of the LoginPage and perform the user login
    login_page = LoginPage(driver)
    login_page.user_login()
    sleep(5)

    # Create an instance of the AccountsPage and select the specified account number
    accounts_page = AccountsPage(driver)
    accounts_page.select_account(account_number)
    # Create an instance of the AccountsInfo page
    account_info_page = AccountsInfo(driver)
    # Call the AccountInfo method to retrieve the account information for the specified account number
    account_info_page.AccountInfo(account_number)
    # Call the get_account_info method to retrieve the account information
    account_info = account_info_page.get_account_info(account_number)
    # Get the expected account information based on the specified account number
    expected_account_info = expected_info.get(account_number, {})

    # Iterate over the expected account information and compare it with the retrieved account information
    for key, value in expected_account_info.items():
        assert account_info.get(key) == value

    # Log the account information for the specified account number
    logger.info(f"Account Info for {account_number}:")
    logger.info(f"Holder Name: {account_info.get('holder_name')}")
    logger.info(f"Currency: {account_info.get('currency')}")
    logger.info(f"Status: {account_info.get('status')}")
    logger.info(f"Account Type: {account_info.get('account_type')}")
