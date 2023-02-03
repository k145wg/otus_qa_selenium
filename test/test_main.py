from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAGE_NAME = "/index.php"


def test_currency(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.ID, "form-currency")))
    assert el.text == '$ Currency '


def test_search(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.ID, "search")))
    assert el.text == ''


def test_logo(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "logo")))


def test_cart(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(EC.presence_of_element_located((By.ID, "cart")))
    assert el.text == "0 item(s) - $0.00"
    el.click()
    el = wait.until(EC.presence_of_element_located((By.ID, "cart")))
    assert el.text == "0 item(s) - $0.00\nYour shopping cart is empty!"


def test_my_account(browser):
    address = browser.url + PAGE_NAME

    register_xpath = "//a[@href='" + address + "?route=account/register']"
    login_xpath = "//a[@href='" + address + "?route=account/login']"

    browser.get(address)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.invisibility_of_element_located((By.XPATH, register_xpath)))
    wait.until(EC.invisibility_of_element_located((By.XPATH, login_xpath)))
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@title='My Account']")))
    element.click()
    element = wait.until(EC.visibility_of_element_located((By.XPATH, register_xpath)))
    assert element.text == "Register"
    element = wait.until(EC.visibility_of_element_located((By.XPATH, login_xpath)))
    assert element.text == "Login"
