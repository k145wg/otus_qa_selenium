from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src import helpers


class RegisterPage:
    def __init__(self, browser):
        self.browser = browser
        self.address = self.browser.url + "/index.php?route=account/register"
        self.browser.get(self.address)
        self.wait = WebDriverWait(browser, 3, poll_frequency=1)

    def get_privacy_agree_alert(self):
        checkbox = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name=\"agree\"]")))
        checked = checkbox.is_selected()
        if (checked):
            checkbox.click()
        button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class=\"btn btn-primary\"]")))
        button.click()
        return self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-danger alert-dismissible\"]")))

    def get_privacy_policy(self):
        link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class=\"agree\"]")))
        link.click()
        title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[@class=\"modal-title\"]")))
        body = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class=\"modal-body\"]")))
        return title, body

    def get_password(self, password=None):
        self.browser.refresh()
        element = self.wait.until(EC.presence_of_element_located((By.ID, "input-password")))
        if password is None:
            return element
        element.send_keys(password)
        return self.wait.until(EC.presence_of_element_located((By.ID, "input-password")))

    def get_confirm_password(self, confirm_password=None):
        self.browser.refresh()
        element = self.wait.until(EC.presence_of_element_located((By.ID, "input-confirm")))
        if confirm_password is None:
            return element
        element.send_keys(confirm_password)
        return self.wait.until(EC.presence_of_element_located((By.ID, "input-confirm")))

    def _send_personal_data(self):
        firstname = helpers.random_string(7)
        lastname = helpers.random_string(12)
        el = self.wait.until(EC.presence_of_element_located((By.ID, "input-firstname")))
        el.send_keys(firstname)
        el = self.wait.until(EC.presence_of_element_located((By.ID, "input-lastname")))
        el.send_keys(lastname)
        el = self.wait.until(EC.presence_of_element_located((By.ID, "input-email")))
        el.send_keys(helpers.random_email())
        el = self.wait.until(EC.presence_of_element_located((By.ID, "input-telephone")))
        el.send_keys(helpers.random_digits(10))
        checkbox = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name=\"agree\"]")))
        checked = checkbox.is_selected()
        if (not checked):
            checkbox.click()
        return firstname, lastname

    def _set_password(self):
        password = helpers.random_password(14)
        el = self.wait.until(EC.presence_of_element_located((By.ID, "input-password")))
        el.send_keys(password)
        el = self.wait.until(EC.presence_of_element_located((By.ID, "input-confirm")))
        el.send_keys(password)
        return password

    def get_diff_pass_confirm_alert(self, password=None, confirm_password=None):
        self.browser.get(self.address)
        self._send_personal_data()
        if password is not None:
            el = self.wait.until(EC.presence_of_element_located((By.ID, "input-password")))
            el.send_keys(password)
        if confirm_password is not None:
            el = self.wait.until(EC.presence_of_element_located((By.ID, "input-confirm")))
            el.send_keys(confirm_password)
        button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class=\"btn btn-primary\"]")))
        button.click()
        return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class=\"text-danger\"]")))

    def add_new_user(self):
        self.browser.get(self.address)
        firstname, lastname = self._send_personal_data()
        password = self._set_password()
        button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class=\"btn btn-primary\"]")))
        button.click()
        return {'firstname': firstname, 'lastname': lastname, 'password': password}
