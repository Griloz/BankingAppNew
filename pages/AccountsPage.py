from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from logs.logger import logger
from time import sleep

# create a class for the page


class AccountsPage(BasePage):

    # create a method that performs actions on the page
    def select_account(self, account_number):
        # find and click the dropdown
        self.driver.find_element(
            By.CSS_SELECTOR, "[formcontrolname='accountId']").click()
        sleep(5)

        # find the account number element
        self.driver.find_element(
            By.XPATH, f"//span[text()='{account_number}']").click()
        sleep(5)


class AccountsInfo(BasePage):
    def AccountInfo(self, account_info_number):
        current_balance = self.driver.find_element(
            By.XPATH, "//div[text()='Current Balance']/following-sibling::div[2]").text
        currency = self.driver.find_element(
            By.XPATH, "//div[text()='Currency']/following-sibling::div").text
        status = self.driver.find_element(
            By.XPATH, "//div[text()='Status']/following-sibling::div").text
        account_type = self.driver.find_element(
            By.XPATH, "//div[text()='Account type']/following-sibling::div").text
        holder_name = self.driver.find_element(
            By.XPATH, "//span[contains(text(), 'John Doe')]").text.split(", ")[1]

        # Create the account_info dictionary with the retrieved information
        account_info = {
            'current_balance': current_balance,
            'currency': currency,
            'status': status,
            'account_type': account_type,
            'holder_name': holder_name  # Add holder_name to the account_info dictionary
        }

        return account_info

    def get_account_info(self, account_info_number):
        # Call the AccountInfo method to retrieve the account information
        return self.AccountInfo(account_info_number)
