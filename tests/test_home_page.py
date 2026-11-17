import pytest

from pages.Home_page import homepage

def test_sign_page(driver):
    home_page = homepage(driver)
    home_page.open_HP()

    assert "https://authorized-partner.vercel.app/" in driver.current_url

def test_GS_btn(driver):
    home_page = homepage(driver)
    home_page.open_HP()
    home_page.get_Started_btn()

    assert "https://authorized-partner.vercel.app/register" in driver.current_url