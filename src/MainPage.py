from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.address = self.browser.url + "/index.php"
        self.browser.get(self.address)
        self.wait = WebDriverWait(browser, 3, poll_frequency=1)

    def get_form_currency(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "form-currency")))

    def change_currency(self, currency='Euro'):
        self.browser.find_element_by_css_selector(
            "#form-currency > div:nth-child(1) > button:nth-child(1) > span:nth-child(2)").click()
        elements = self.browser.find_elements_by_css_selector(".open > ul:nth-child(2) > li")
        for element in elements:
            if currency in element.text:
                element.click()
                return currency
        return ""

    def get_search(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "search")))

    def get_logo(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "logo")))

    def get_cart_text(self):
        self.browser.refresh()
        cart_element = self.wait.until(EC.presence_of_element_located((By.ID, "cart")))
        return cart_element.text

    def get_cart_empty_text(self):
        self.browser.refresh()
        cart_element_empty = self.wait.until(EC.presence_of_element_located((By.ID, "cart")))
        cart_element_empty.click()
        return cart_element_empty.text

    def get_my_account(self):
        register_xpath = "//a[@href='" + self.address + "?route=account/register']"
        login_xpath = "//a[@href='" + self.address + "?route=account/login']"
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, register_xpath)))
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, login_xpath)))
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@title='My Account']")))
        element.click()
        register_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, register_xpath)))
        login_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, login_xpath)))
        return register_element, login_element

    def add_to_cart(self):
        elements = self.browser.find_elements_by_css_selector("div.product-layout")
        elements[0].find_element_by_css_selector("button:nth-child(1)").click()
