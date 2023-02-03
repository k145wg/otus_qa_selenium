from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAGE_NAME = "/admin"


# panel-title
def test_admin_panel_title(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='panel-title']")))
    assert el.text == 'Please enter your login details.'


def test_empty_credits(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    el = wait.until(EC.presence_of_element_located((By.ID, "input-username")))
    assert el.text == ''
    el = wait.until(EC.presence_of_element_located((By.ID, "input-password")))
    assert el.text == ''


def test_mask_password(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    el = wait.until(EC.presence_of_element_located((By.ID, "input-password")))
    el.send_keys("qwerty")
    el = wait.until(EC.presence_of_element_located((By.ID, "input-password")))
    assert el.text == ''


def test_enter_with_empty_pass(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    batton = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class=\"btn btn-primary\"]")))
    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-danger alert-dismissible\"]")))
    batton.click()
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-danger alert-dismissible\"]")))
    assert element.text == 'No match for Username and/or Password.\n×'


def test_forgotten(browser):
    address = browser.url + PAGE_NAME
    forgotten_xpath = "//a[@href='" + address + "/index.php?route=common/forgotten']"
    browser.get(address)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.XPATH, forgotten_xpath)))
    assert el.text == 'Forgotten Password'
    el.click()
    el = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='panel-title']")))
    assert el.text == 'Forgot Your Password?'
