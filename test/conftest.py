import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox", help="browser to run tests")
    parser.addoption("--drivers", default=os.path.expanduser("/home/olapshikov/drivers/"))
    # headless-режиме, то есть без создания визуального окна браузера
    parser.addoption("--headless", action="store_true", help="browser to run tests")
    parser.addoption("--base_url", default="http://192.168.43.46:55555", help="browser to run tests")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    driver_path = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.c = False  # True
        service = ChromeService(executable_path=os.path.join(driver_path, "chromedriver"))
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        if headless:
            options.c = True
        service = ChromeService(executable_path=os.path.join(driver_path, "yandexdriver"))
        options.binary_location = "/usr/bin/yandex-browser"
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=os.path.join(driver_path, "geckodriver"))
    elif browser == "safari":
        driver = webdriver.Safari()
    elif browser == "opera":
        driver = webdriver.Chrome(executable_path=os.path.join(driver_path, "operadriver"))
    else:
        raise Exception("Driver not supported")

    driver.url = base_url
    driver.maximize_window()
    yield driver
    driver.close()
