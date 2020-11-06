from utilities.base_test import BaseTest
from utilities.loggers import log_message
from objects.account_page import AccountPage
from common import test_data
from objects.shop_page import ShopPage
from common import helpers

import time

class AccountTests(BaseTest):
    def setUp(self):
        super().setUp()
        self.account_page = AccountPage(self.driver)
        self.shop_page = ShopPage(self.driver)

    def test_register_new_user(self):
        log_message("Register new user")

        timestamp_random = helpers.get_timestamp()

        self.account_page.navigate_to_page()
        self.account_page.store_name_input.send_keys("Andrej" + timestamp_random)
        self.account_page.password_input.send_keys(test_data.VALID_PASSWORD)
        self.account_page.register_button.click()

        time.sleep(5)

        self.assertTrue(self.account_page.info_label.text == "User registered")

    def test_login_without_store_name(self):
        log_message("Test without store name")

        self.account_page.navigate_to_page()
        self.account_page.password_input.send_keys(test_data.VALID_PASSWORD)
        self.account_page.register_button.click()

        time.sleep(5)

        self.assertTrue(self.account_page.info_label.text == "Input fields can't be blank")

    def test_registration_with_same_user(self):
        log_message("Test registration with existing username")

        timestamp_random = helpers.get_timestamp()

        self.account_page.navigate_to_page()
        self.account_page.store_name_input.send_keys(test_data.VALID_STORE_NAME)
        self.account_page.password_input.send_keys(test_data.VALID_PASSWORD)
        self.account_page.register_button.click()

        time.sleep(5)

        self.assertTrue(self.account_page.info_label.text == "User already exists")

    def test_cant_login_with_wrong_pass(self):
        log_message("Cannot login with wrong password")

        self.account_page.navigate_to_page()
        self.account_page.store_name_input.send_keys(test_data.VALID_STORE_NAME)
        self.account_page.password_input.send_keys(test_data.INVALID_PASSWORD)
        self.account_page.login_button.click()

        time.sleep(5)

        self.assertTrue(self.account_page.info_label.text == "Wrong password, try again.")

    def test_deletion_incorrect_password(self):
        log_message("Test 5 - Cannot delete account with incorrect password")

        self.account_page.navigate_to_page()
        self.account_page.store_name_input.send_keys(test_data.VALID_STORE_NAME)
        self.account_page.password_input.send_keys(test_data.INVALID_PASSWORD)
        self.account_page.delete_button.click()

        time.sleep(5)

        self.assertTrue(self.account_page.info_label.text == "Wrong password, try again.")

    def test_successful_login(self):
        log_message("TEST 6 - Logirati se u aplikaciju")

        self.account_page.navigate_to_page()
        self.account_page.login(test_data.VALID_STORE_NAME, test_data.VALID_PASSWORD)
        self.shop_page.wait_for_shop_to_load()
        self.shop_page.save_screenshot("test_successful_login")
        self.assertTrue(self.shop_page.empty_order_button)