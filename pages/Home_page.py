from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class homepage(BasePage):

    gs_Button = (By.XPATH, "/html[1]/body[1]/div[4]/header[1]/div[1]/div[1]/a[2]/button[1]")

    def open_HP(self):
        self.driver.get("https://authorized-partner.vercel.app/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self

    def get_Started_btn(self):
        self.click(self.gs_Button)
        return self