from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAGE_NAME = "/admin"

from src.AdminPage import AdminPage


def test_admin_panel_title(browser):
    adminPage = AdminPage(browser)
    element = adminPage.get_admin_panel()
    assert element.text == 'Please enter your login details.'


def test_empty_credits(browser):
    adminPage = AdminPage(browser)
    input_username_element, input_password_element = adminPage.get_input_credits()
    assert input_username_element.text == ''
    assert input_password_element.text == ''


def test_mask_password(browser):
    adminPage = AdminPage(browser)
    input_password = adminPage.get_password('qwerty')
    assert input_password.text == ''


def test_enter_with_empty_pass(browser):
    adminPage = AdminPage(browser)
    alert = adminPage.get_enter_with_empty_pass_alert()
    assert alert.text == 'No match for Username and/or Password.\n×'


def test_forgotten(browser):
    adminPage = AdminPage(browser)
    get_forgotten_panel = adminPage.get_forgotten_panel()
    assert get_forgotten_panel.text == 'Forgot Your Password?'
