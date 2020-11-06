from utilities.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ShopPage(BasePage):

    slug = "/store/"
    empty_order_button_locator = (By.CSS_SELECTOR, "[data-testid=empty-order-button]")
    load_bugs_button_locator = (By.CSS_SELECTOR, "[data-testid=load-sample-bugs-button]")
    bugs_lists_locator = (By.CSS_SELECTOR, "[data-testid=bug-shop-item]")
    bug_remove_locator = (By.CSS_SELECTOR, "[data-testid=bug-remove-button]")
    bug_name_locator = (By.CSS_SELECTOR, "[data-testid=bug-shop-input]")
    bug_name_selection_locator = (By.CSS_SELECTOR, "[data-testid=bug-shop-name]")
    bug_name_inputs_locator = (By.CSS_SELECTOR, "[data-testid=bug-name-input]")
    clear_inventory_button_locator = (By.CSS_SELECTOR, "[data-testid=clear-inventory-button]")
    bug_status_button_locator = (By.CSS_SELECTOR, "[data-testid=bug-status-input]")
    bug_price_input_locator = (By.CSS_SELECTOR, "[data-testid=bug-price-input]")
    bug_description_input_locator = (By.CSS_SELECTOR, "[data-testid=bug-description-input]")
    bug_name_input_locator = (By.CSS_SELECTOR, "[data-testid=bug-name-input]")
    add_bug_button_locator = (By.CSS_SELECTOR, "[data-testid=bug-submit-button]")
    bug_price_locator = (By.CSS_SELECTOR, "[data-testid=bug-shop-price]")
    bug_description_locator = (By.CSS_SELECTOR, "[data-testid=bug-shop-name]")
    add_to_order_locator = (By.CSS_SELECTOR, "[data-testid=add-to-order-button]")
    bug_in_order_locator = (By.CSS_SELECTOR, "[data-testid=order-item]")
    total_price_locator = (By.CSS_SELECTOR, "[data-testid=total-price]")
    order_item_locator = (By.CSS_SELECTOR, "[data-testid=order-item]")


    def navigate_to_page(self, store_name):
        self.navigate(self.slug + store_name)

    def wait_for_bugs_to_load(self):
        self.wait_until_element_present(self.bug_remove_locator)

    @property
    def bug_remove_buttons(self):
        return self.get_present_elements(self.bug_remove_locator)


    @property
    def empty_order_button(self):
        return self.get_present_element(self.empty_order_button_locator)

    def wait_for_shop_to_load(self):
        self.wait_until_element_present(self.empty_order_button_locator)

    @property
    def load_bugs_button(self):
        return self.get_present_element(self.load_bugs_button_locator)

    @property
    def bugs_list_items(self):
        return self.get_present_elements(self.bugs_lists_locator)

    @property
    def remove_bug_button(self):
        return self.get_present_element(self.bug_remove_locator)

    @property
    def bug_names_in_selection(self):
        return self.get_present_elements(self.bug_name_selection_locator)

    @property
    def bug_name_in_selection(self):
        return self.get_present_element(self.bug_name_selection_locator)

    @property
    def bug_name_inputs(self):
        return self.get_present_elements(self.bug_name_inputs_locator)

    @property
    def clear_inventory_button(self):
        return self.get_present_element(self.clear_inventory_button_locator)

    def remove_bug_with_name(self, trazeni_bug):
        bug_list = self.bug_name_inputs
        index = 0
        for bug in bug_list:
            if bug.get_attribute("value") == trazeni_bug:
                index = bug_list.index(bug)
        remove_button_list = self.bug_remove_buttons
        remove_button_list[index].click()

    def is_bug_in_selection(self, bug_name):
        selection_list = self.bug_names_in_selection
        for bug in selection_list:
            if bug.text.split()[0] == bug_name:
                return True

        return False

    @property
    def change_bug_status_dropdowns(self):
        return self.get_present_elements(self.bug_status_button_locator)

    def change_bug_status(self, bug_name, bug_status):
        all_bug_names_list = self.bug_name_inputs
        index = 0
        for bug in all_bug_names_list:
            if bug.get_attribute("value") == bug_name:
                index = all_bug_names_list.index(bug)
        bug_status_dropdown = Select(self.change_bug_status_dropdowns[index])
        bug_status_dropdown.select_by_visible_text(bug_status)

    @property
    def bug_name_inputs(self):
        return self.get_present_elements(self.bug_name_inputs_locator)

    @property                           #za test 12
    def bug_price_input(self):
        return self.get_present_element(self.bug_price_input_locator)

    @property                           #za test 12
    def bug_description_input(self):
        return self.get_present_element(self.bug_description_input_locator)

    @property                           #za test 12
    def bug_name_input(self):
        return self.get_present_element(self.bug_name_input_locator)

    @property                           #za test 12
    def add_bug_button(self):
        return self.get_present_element(self.add_bug_button_locator)

    def enter_bug_details(self, bug_name, bug_price, bug_description):             #test 12
        self.bug_name_input.send_keys(bug_name)
        self.bug_price_input.send_keys(bug_price)
        self.bug_description_input.send_keys(bug_description)
        self.add_bug_button.click()

    @property
    def add_to_order_button(self):                                           #TEST 13
        return self.get_present_elements(self.add_to_order_locator)

    def make_fresh_and_add_bug_to_order(self, bug_name, bug_status):        #TEST 13
        list_of_all_bugs = self.bug_name_inputs
        index = 0
        for bug in list_of_all_bugs:
            if bug.get_attribute("value") == bug_name:
                index = list_of_all_bugs.index(bug)
        bug_status_dropdown = Select(self.change_bug_status_dropdowns[index])
        bug_status_dropdown.select_by_visible_text(bug_status)
        add_bug_to_order = self.add_to_order_button
        add_bug_to_order[index].click()

    @property
    def bug_in_order(self):
        return self.get_present_elements(self.bug_in_order_locator)

    @property
    def bug_price(self):                                            #test 13
        return self.get_present_elements(self.bug_price_locator)

    def get_bug_price(self, bug_name):                              #test 13
        list_of_all_bugs = self.bug_name_inputs
        list_of_all_bug_prices = self.bug_price
        index = 0
        for bug in list_of_all_bugs:
            if bug.get_attribute("value") == bug_name:
                index = list_of_all_bugs.index(bug)
        return round(float(list_of_all_bug_prices[index].text.split("$")[1]), 2)

    @property
    def total_price(self):                                          #test 13
        return self.get_present_element(self.total_price_locator)

    def get_total_price(self):                                      #test 13
        return float(self.total_price.text.split("$")[1])

    def add_bug_to_order(self, bug_name):                           #test 14
        all_bug_names_list = self.bug_name_inputs
        index = 0
        for bug in all_bug_names_list:
            if bug.get_attribute("value") == bug_name:
                index = all_bug_names_list.index(bug)
        add_bug_to_order = self.add_to_order_button
        add_bug_to_order[index].click()

    @property                                                       #test 14
    def order_item_list(self):
        return self.get_present_elements(self.order_item_locator, timeout=5)
