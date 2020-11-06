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

    def test_add_bugs(self):
        log_message("TEST 7 - dodajte bugs u Inventory i provjerite da je lista populated")

        timestamp = helpers.get_timestamp()

        self.account_page.navigate_to_page()
        self.account_page.register_and_login(test_data.VALID_STORE_NAME + timestamp, test_data.VALID_PASSWORD)
        self.shop_page.load_bugs_button.click()
        time.sleep(5)
        self.assertTrue(len(self.shop_page.bugs_list_items) > 0)

    def test_remove_bugs_and_check_count(self):
        log_message("TEST 8 - Maknite prvu bubu iz Inventorya i provjerite da je broj buba u selectionu manji za 1")

        self.account_page.navigate_to_page()
        self.account_page.login(test_data.VALID_STORE_NAME, test_data.VALID_PASSWORD)
        self.shop_page.load_bugs_button.click()

        number_of_bugs_before = len(self.shop_page.bugs_list_items)
        self.shop_page.remove_bug_button.click()

        number_of_bugs_after = len(self.shop_page.bugs_list_items)
        self.assertTrue(number_of_bugs_before-number_of_bugs_after == 1)

    def test_remove_specific_bug(self):
        log_message("TEST 9 - Maknite specifičnu bubu iz inventorija i provjerite da baš nje nema")

        bug_name = "Ants"

        self.account_page.navigate_to_page()
        self.account_page.login(test_data.VALID_STORE_NAME, test_data.VALID_PASSWORD)
        self.shop_page.wait_for_shop_to_load()
        self.shop_page.load_bugs_button.click()

        self.shop_page.wait_for_bugs_to_load()
        self.shop_page.remove_bug_with_name(bug_name)
        time.sleep(5)
        self.account_page.save_screenshot("test_removing_specific_bug_from_inventory")
        self.assertFalse(self.shop_page.is_bug_in_selection(bug_name))
        self.assertTrue(self.shop_page.is_bug_in_selection("Beetle"))

    def test_remove_all_bugs(self):
        log_message("TEST 10 - maknite sve bube iz inventorija i provjerite da ih nema")

        timestamp = helpers.get_timestamp()

        self.account_page.navigate_to_page()
        self.account_page.register_and_login(test_data.VALID_STORE_NAME + timestamp, test_data.VALID_PASSWORD)
        self.shop_page.wait_for_shop_to_load()
        self.shop_page.load_bugs_button.click()
        self.shop_page.wait_for_bugs_to_load()
        self.shop_page.clear_inventory_button.click()

        self.assertFalse(self.shop_page.bug_names_in_selection)

    def test_change_bug_status_and_check_order(self):
        log_message("TEST 11 - Promijenite status odeređene bube i provjerite da ju nije moguce dodati u Order")

        timestamp = helpers.get_timestamp()

        self.account_page.navigate_to_page()
        self.account_page.register_and_login(test_data.VALID_STORE_NAME + timestamp, test_data.VALID_PASSWORD)
        self.shop_page.wait_for_shop_to_load()
        self.shop_page.load_bugs_button.click()
        self.shop_page.wait_for_bugs_to_load()

        self.shop_page.change_bug_status("Ants", "Sold Out")

        self.shop_page.save_screenshot("test_adding_sold_out_bugs")
        time.sleep(10)
        #self.assertFalse(self.shop_page.is_bug_available("Ants"))

    def test_add_own_bug_and_check_details(self):
        log_message("TEST 12 - Dodajte svoju bubu te provjerite ispravnost imena, cijene i opisa")

        bug_name = "Buba"
        bug_price = "9050"
        bug_description = "It's the most exclusive bug ever!"

        timestamp = helpers.get_timestamp()

        self.account_page.navigate_to_page()
        self.account_page.register_and_login(test_data.VALID_STORE_NAME + timestamp, test_data.VALID_PASSWORD)
        self.shop_page.wait_for_shop_to_load()

        self.shop_page.enter_bug_details(bug_name, bug_price, bug_description)
        self.assertTrue(self.shop_page.bug_name_in_selection.text.split("\n")[0] == "Buba")
        self.assertTrue(self.shop_page.bug_price.text == "$90.50")

    def test_add_three_bugs_and_check_total(self):
        log_message("TEST 13 - Dodajte 3 bube i provjerite ispravnost totala")

        timestamp = helpers.get_timestamp()

        bug_one = "Beetle"
        bug_two = "Caterpillar"
        bug_three ="Ladybug"
        bug_status = "Fresh!"

        self.account_page.navigate_to_page()
        self.account_page.register_and_login(test_data.VALID_STORE_NAME + timestamp, test_data.VALID_PASSWORD)
        self.shop_page.wait_for_shop_to_load()
        self.shop_page.load_bugs_button.click()
        self.shop_page.wait_for_bugs_to_load()

        self.shop_page.make_fresh_and_add_bug_to_order(bug_one, bug_status)
        self.shop_page.make_fresh_and_add_bug_to_order(bug_two, bug_status)
        self.shop_page.make_fresh_and_add_bug_to_order(bug_three, bug_status)
        time.sleep(5)

        price_total = round((self.shop_page.get_bug_price(bug_one) + self.shop_page.get_bug_price(bug_two)+ self.shop_page.get_bug_price(bug_three)), 2)
        print(self.shop_page.get_bug_price(bug_one))
        print(self.shop_page.get_bug_price(bug_two))
        print(self.shop_page.get_bug_price(bug_three))
        print(price_total)
        print(self.shop_page.get_total_price())

        self.assertTrue(self.shop_page.get_total_price() == price_total)

        #probati riješiti za rangevima [1:]

    def test_add_bug_empty_order_check_order_empty(self):
        log_message("TEST 14 - dodajde bug order, ispraznite i provjerite da je prazan")

        timestamp = helpers.get_timestamp()
        bug_name = "Beetle"

        self.account_page.navigate_to_page()
        self.account_page.register_and_login(test_data.VALID_STORE_NAME + timestamp, test_data.VALID_PASSWORD)
        self.shop_page.wait_for_shop_to_load()
        self.shop_page.load_bugs_button.click()
        self.shop_page.wait_for_bugs_to_load()

        self.shop_page.add_bug_to_order(bug_name)
        self.shop_page.empty_order_button.click()

        self.assertFalse(self.shop_page.order_item_list)
        #print(self.shop_page.bugs_list_items)
        #print(bugs_in_order_list)

        self.assertTrue(self.shop_page.total_price.text == "$0.00")

