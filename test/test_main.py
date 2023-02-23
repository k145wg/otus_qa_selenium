from src.MainPage import MainPage


def test_currency(browser):
    mainPage = MainPage(browser)
    el = mainPage.get_form_currency()
    assert el.text == '$ Currency '


def test_search(browser):
    mainPage = MainPage(browser)
    el = mainPage.get_search()
    assert el.text == ''


def test_logo(browser):
    mainPage = MainPage(browser)
    mainPage.get_logo()


def test_cart(browser):
    mainPage = MainPage(browser)
    cart_element_text = mainPage.get_cart_text()
    assert cart_element_text == "0 item(s) - $0.00"
    cart_element_empty_text = mainPage.get_cart_empty_text()
    assert cart_element_empty_text == "0 item(s) - $0.00\nYour shopping cart is empty!"


def test_my_account(browser):
    mainPage = MainPage(browser)
    register_element, login_element = mainPage.get_my_account()
    assert register_element.text == "Register"
    assert login_element.text == "Login"
