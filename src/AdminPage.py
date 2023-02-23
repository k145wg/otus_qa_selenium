from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    def __init__(self, browser):
        self.browser = browser
        self.address = self.browser.url + "/admin"
        self.browser.get(self.address)
        self.wait = WebDriverWait(browser, 3, poll_frequency=1)

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
