from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage:
    def __init__(self, browser):
        self.browser = browser
        self.address = self.browser.url + "/smartphone"
        self.browser.get(self.address)
        self.wait = WebDriverWait(browser, 3, poll_frequency=1)

    def get_link(self):
        address_xpath = "//a[@href=\"" + self.address + "\"]"
        return self.wait.until(EC.presence_of_element_located((By.XPATH, address_xpath)))

    def get_product_cards(self):
        address_xpath = "//div[@class=\"product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12\"]"
        return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, address_xpath)))

    def get_compare_total(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "compare-total")))

    def get_input_sort(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "input-sort")))

    def get_input_limit(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "input-limit")))
