from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAGE_NAME = "/index.php?route=account/register"


def test_privacy_agree(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-danger alert-dismissible\"]")))
    button = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class=\"btn btn-primary\"]")))
    button.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-danger alert-dismissible\"]")))
    checkbox = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name=\"agree\"]")))
    checkbox.click()
    button = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class=\"btn btn-primary\"]")))
    button.click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-danger alert-dismissible\"]")))


def test_privacy_policy(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class=\"agree\"]")))
    link.click()
    title = wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[@class=\"modal-title\"]")))
    assert title.text == "Privacy Policy"
    body = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class=\"modal-body\"]")))
    assert body.text == "Privacy Policy"


def test_mask_password(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    el = wait.until(EC.presence_of_element_located((By.ID, "input-password")))
    el.send_keys("qwerty")
    el = wait.until(EC.presence_of_element_located((By.ID, "input-password")))
    assert el.text == ''


def test_mask_confirm_password(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    el = wait.until(EC.presence_of_element_located((By.ID, "input-confirm")))
    el.send_keys("qwerty")
    el = wait.until(EC.presence_of_element_located((By.ID, "input-confirm")))
    assert el.text == ''


def test_diff_pass_confirm(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    el = wait.until(EC.presence_of_element_located((By.ID, "input-firstname")))
    el.send_keys("Ivan")
    el = wait.until(EC.presence_of_element_located((By.ID, "input-lastname")))
    el.send_keys("Petrov")
    el = wait.until(EC.presence_of_element_located((By.ID, "input-email")))
    el.send_keys("petrov@example.com")
    el = wait.until(EC.presence_of_element_located((By.ID, "input-telephone")))
    el.send_keys("+0 (123) 456-78-90")
    el = wait.until(EC.presence_of_element_located((By.ID, "input-password")))
    el.send_keys("qwerty")
    el = wait.until(EC.presence_of_element_located((By.ID, "input-confirm")))
    el.send_keys("123456")
    checkbox = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name=\"agree\"]")))
    checkbox.click()
    button = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class=\"btn btn-primary\"]")))
    button.click()
    error_texts = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class=\"text-danger\"]")))
    assert len(error_texts) == 1
    assert error_texts[0].text == "Password confirmation does not match password!"
