from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAGE_NAME = "/smartphone"


def test_link(browser):
    address = browser.url + PAGE_NAME
    address_xpath = "//a[@href=\"" + address + "\"]"

    browser.get(address)
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.presence_of_element_located((By.XPATH, address_xpath)))
    assert el.text == 'Phones & PDAs'


def test_product_cards(browser):
    address = browser.url + PAGE_NAME
    address_xpath = "//div[@class=\"product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12\"]"

    browser.get(address)
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    el = wait.until(EC.presence_of_all_elements_located((By.XPATH, address_xpath)))
    assert len(el) == 3


def test_compare_total(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.ID, "compare-total")))
    assert el.text == 'Product Compare (0)'


def test_input_sort(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.ID, "input-sort")))
    assert el.text == "Default\nName (A - Z)\nName (Z - A)\nPrice (Low > High)\nPrice (High > Low)\nRating (" \
                      "Highest)\nRating (Lowest)\nModel (A - Z)\nModel (Z - A)"


def test_input_limit(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.ID, "input-limit")))
    assert el.text == "20\n25\n50\n75\n100"
