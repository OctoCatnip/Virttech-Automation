from selenium import webdriver
import pytest


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()