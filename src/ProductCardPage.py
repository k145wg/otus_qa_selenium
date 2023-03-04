from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductCardPage:
    def __init__(self, browser):
        self.browser = browser
        self.address = self.browser.url + "//laptop-notebook/hp-lp3065"
        self.browser.get(self.address)
        self.wait = WebDriverWait(browser, 3, poll_frequency=1)

    def get_tab_description(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "tab-description")))

    def get_tab_specification(self):
        self.wait.until(EC.invisibility_of_element_located((By.ID, "tab-specification")))
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href=\"#tab-specification\"]")))
        element.click()
        return self.wait.until(EC.visibility_of_element_located((By.ID, "tab-specification")))

    def get_tab_review(self):
        self.wait.until(EC.invisibility_of_element_located((By.ID, "tab-review")))
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href=\"#tab-review\"]")))
        element.click()
        return self.wait.until(EC.visibility_of_element_located((By.ID, "tab-review")))

    def add_to_wish(self):
        self.wait.until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-success alert-dismissible\"]")))
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@onclick=\"wishlist.add('47');\"]")))
        element.click()
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-success alert-dismissible\"]")))

    def add_to_compare(self):
        self.wait.until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-success alert-dismissible\"]")))
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@onclick=\"compare.add('47');\"]")))
        element.click()
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-success alert-dismissible\"]")))
