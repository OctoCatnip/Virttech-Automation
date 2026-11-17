import pytest

from pages.Home_page import homepage
from pages.agree_page import AgreePage

def test_agree_page(driver):
    home_page = homepage(driver)
    home_page.open_HP()
    home_page.get_Started_btn()

    agree_page = AgreePage(driver)
    agree_page.get_Agree_checkbox()
    agree_page.get_Ctn_btn()

    assert agree_page.get_Heading_text() == "Complete Your Agent Profile in Steps"