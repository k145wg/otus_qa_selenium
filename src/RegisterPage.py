from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        el = self.wait.until(EC.presence_of_element_located((By.ID, "input-firstname")))
        el.send_keys("Ivan")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "input-lastname")))
        el.send_keys("Petrov")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "input-email")))
        el.send_keys("petrov@example.com")
        el = self.wait.until(EC.presence_of_element_located((By.ID, "input-telephone")))
        el.send_keys("+0 (123) 456-78-90")
        checkbox = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name=\"agree\"]")))
        checked = checkbox.is_selected()
        if (not checked):
            checkbox.click()

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
