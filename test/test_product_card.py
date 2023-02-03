from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAGE_NAME = "/laptop-notebook/hp-lp3065"


def test_tab_description(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    el = wait.until(EC.visibility_of_element_located((By.ID, "tab-description")))
    assert el.text == "Stop your co-workers in their tracks with the stunning new 30-inch diagonal HP LP3065 Flat " \
                      "Panel Monitor. This flagship monitor features best-in-class performance and presentation " \
                      "features on a huge wide-aspect screen while letting you work as comfortably as possible - you " \
                      "might even forget you're at the office"


def test_tab_specification(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    wait.until(EC.invisibility_of_element_located((By.ID, "tab-specification")))
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href=\"#tab-specification\"]")))
    element.click()
    wait.until(EC.visibility_of_element_located((By.ID, "tab-specification")))


def test_tab_review(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 3, poll_frequency=1)
    wait.until(EC.invisibility_of_element_located((By.ID, "tab-review")))
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href=\"#tab-review\"]")))
    element.click()
    wait.until(EC.visibility_of_element_located((By.ID, "tab-review")))


def test_add_to_wish(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 1, poll_frequency=1)
    wait.until(
        EC.invisibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-success alert-dismissible\"]")))
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@onclick=\"wishlist.add('47');\"]")))
    element.click()
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-success alert-dismissible\"]")))
    assert element.text == "You must login or create an account to save HP LP3065 to your wish list!\n×"


def test_add_to_compare(browser):
    browser.get(browser.url + PAGE_NAME)
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    wait.until(
        EC.invisibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-success alert-dismissible\"]")))
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@onclick=\"compare.add('47');\"]")))
    element.click()
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class=\"alert alert-success alert-dismissible\"]")))
    assert element.text == "Success: You have added HP LP3065 to your product comparison!\n×"
