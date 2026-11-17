import time

import pytest

from pages.Home_page import homepage
from pages.agree_page import AgreePage
from pages.sign_page import SignPage
from pages.otp_page import OtpPage
from pages.agent_Detail_page import AgentDetailPage
from pages.exp_per_page import ExpPage

from utils.mailtm_otp import MailTm

def test_signin_page(driver):

    email = "lorrayne41@euploading.com"
    mail_password = "W2lR4]KOR,"

    mail = MailTm(email, mail_password)
    mail.login()

    home_page = homepage(driver)
    home_page.open_HP()
    home_page.get_Started_btn()

    # assert "https://authorized-partner.vercel.app/register" in driver.current_url

    agree_page = AgreePage(driver)
    agree_page.get_Agree_checkbox()
    agree_page.get_Ctn_btn()

    # assert agree_page.get_Heading_text() == "Complete Your Agent Profile in Steps"

    sign_page = SignPage(driver)
    otp_requested_at = time.time()
    sign_page.sign_Page_1("lalu", "Sharma", "lorrayne41@euploading.com", "9810000023", "Password123@", "Password123@")

    otp = mail.get_otp(
        since_timestamp=otp_requested_at,
        timeout=90
    )

    print("otp: ", otp)

    otp_page = OtpPage(driver)
    otp_page.enter_otp(otp)
    otp_page.wait_for_next_page()
    print("Current URL", driver.current_url)

    # assert agree_page.get_Heading_text() == "Complete Your Agent Profile in Steps"

    agentDetail_page = AgentDetailPage(driver)
    agentDetail_page.agent_Page("ABC Agent", "CEO", "ABC@gmail.com", "ABCD.com", "test", "Test")

    # assert agree_page.get_Heading_text() == "Experience and Performance Metrics"

    exp_page = ExpPage(driver)
    exp_page.exp_page("10", "Master", "80", "1 year", "Test Prepration")