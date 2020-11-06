from utilities.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountPage(BasePage):

    slug = "/"
    store_name_locator = (By.CSS_SELECTOR, "[data-testid=store-name-input]")
    password_locator = (By.CSS_SELECTOR, "[data-testid=password-input]")
    login_button_locator = (By.CSS_SELECTOR, "[data-testid=login-button]")
    register_button_locator = (By.CSS_SELECTOR, "[data-testid=register-button]")
    delete_button_locator = (By.CSS_SELECTOR, "[data-testid=delete-button]")
    info_label_locator = (By.CSS_SELECTOR, "[data-testid=message]")

    def navigate_to_page(self):
        self.navigate(self.slug)

    @property
    def store_name_input(self):
        return self.get_present_element(self.store_name_locator)

    @property
    def password_input(self):
        return self.get_present_element(self.password_locator)

    @property
    def login_button(self):
        return self.get_present_element(self.login_button_locator)

    @property
    def register_button(self):
        return self.get_present_element(self.register_button_locator)

    @property
    def delete_button(self):
        return self.get_present_element(self.delete_button_locator)

    @property
    def info_label(self):
        return self.get_present_element(self.info_label_locator)

    def login(self, store_name, password):
        self.store_name_input.send_keys(store_name)
        self.password_input.send_keys(password)
        self.login_button.click()

    def register_and_login(self, store_name, password):
        self.store_name_input.send_keys(store_name)
        self.password_input.send_keys(password)
        self.register_button.click()
        self.login_button.click()