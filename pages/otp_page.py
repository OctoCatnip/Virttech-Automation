from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OtpPage(BasePage):

    otp_input = (By.CSS_SELECTOR, "input[data-input-otp='true']")
    verify_btn = (By.XPATH, "//button[@type='submit']")
    header = (By.XPATH, "//h3[@class='text-lg lg:text-xl font-[700] tracking-[-0.4px]']")

    def enter_otp(self, otp):
        self.enter_text(self.otp_input, otp)
        self.click(self.verify_btn)

        return self

    def wait_for_next_page(self):
        self.wait.until(
            EC.url_changes(self.driver.current_url),
        )

    def get_Heading_text(self):
        return self.get_text(self.header)