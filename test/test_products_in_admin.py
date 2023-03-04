from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAGE_NAME = "/admin"

from src.AdminPage import AdminPage


def test_admin_panel_title(browser):
    adminPage = AdminPage(browser)
    product_count = adminPage.find_product('test_product9601', 'test_model764')
    assert product_count == 0

    adminPage.add_product('test_product9601', 'test_model764')
    product_count = adminPage.find_product('test_product9601', 'test_model764')
    assert product_count == 1

    adminPage.delete_product('test_product9601', 'test_model764')
    product_count = adminPage.find_product('test_product9601', 'test_model764')
    assert product_count == 0
