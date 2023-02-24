from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    def __init__(self, browser):
        self.browser = browser
        self.address = self.browser.url + "/admin"
        self.browser.get(self.address)
        self.wait = WebDriverWait(browser, 3, poll_frequency=1)

    def _admin_authorization(self):
        username = 'user'
        password = 'bitnami'
        self.browser.find_element_by_id("input-username").send_keys(username)
        self.browser.find_element_by_id("input-password").send_keys(password)
        self.browser.find_element_by_css_selector("button.btn.btn-primary").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-profile")))

    def _admin_logoff(self):
        self.browser.find_element_by_css_selector(".nav > li:nth-child(2) > a:nth-child(1)").click()

    def _check_product_space(self):
        self.browser.find_element_by_id("menu-catalog").click()
        self.browser.find_elements_by_css_selector("#collapse1 > li")[1].click()

    def add_product(self, product_name, model_name):
        self._admin_authorization()
        self._check_product_space()
        self.browser.find_element_by_css_selector("a.btn:nth-child(2)").click()
        add_product_tabs = self.browser.find_elements_by_css_selector("#form-product > ul:nth-child(1) > li")
        add_product_tabs[0].click()
        self.browser.find_element_by_id("input-name1").send_keys(product_name)
        self.browser.find_element_by_id("input-meta-title1").send_keys(product_name)
        add_product_tabs[1].click()
        self.browser.find_element_by_id("input-model").send_keys(model_name)
        self.browser.find_element_by_css_selector("div.pull-right > button:nth-child(1)").click()
        self._admin_logoff()

    def _set_product_filter(self, product_name, model_name):
        self.browser.find_element_by_id("input-name").send_keys(product_name)
        self.browser.find_element_by_id("input-model").send_keys(model_name)
        self.browser.find_element_by_id("button-filter").click()

    def find_product(self, product_name, model_name):
        self._admin_authorization()
        self._check_product_space()
        self._set_product_filter(product_name, model_name)
        result = self.browser.find_element_by_css_selector("div.col-sm-6:nth-child(2)").text
        result = result.split(" ")
        self._admin_logoff()
        return int(result[5])

    def delete_product(self, product_name, model_name):
        self._admin_authorization()
        self._check_product_space()
        self._set_product_filter(product_name, model_name)

        checkbox = self.browser.find_element_by_css_selector(
            ".table > thead:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)")
        checked = checkbox.is_selected()
        if (not checked):
            checkbox.click()
        self.browser.find_element_by_css_selector("button.btn:nth-child(4)").click()
        self.wait.until(EC.alert_is_present())
        self.browser.switch_to.alert.accept()
        self._admin_logoff()

    def get_admin_panel(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='panel-title']")))

    def get_input_credits(self):
        input_username_element = self.wait.until(EC.presence_of_element_located((By.ID, "input-username")))
        input_password_element = self.wait.until(EC.presence_of_element_located((By.ID, "input-password")))
        return input_username_element, input_password_element

    def get_password(self, password=None):
        self.browser.refresh()
        element = self.wait.until(EC.presence_of_element_located((By.ID, "input-password")))
        if password is None:
            return element
        element.send_keys(password)
        return self.wait.until(EC.presence_of_element_located((By.ID, "input-password")))

    def get_enter_with_empty_pass_alert(self):
        button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class=\"btn btn-primary\"]")))
        self.wait.until(
            EC.invisibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-danger alert-dismissible\"]")))
        button.click()
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-danger alert-dismissible\"]")))

    def get_forgotten_panel(self):
        forgotten_xpath = "//a[@href='" + self.address + "/index.php?route=common/forgotten']"
        forgotten_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, forgotten_xpath)))
        forgotten_link.click()
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='panel-title']")))
