from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class AgreePage(BasePage):

    agree_Checkbox = (By.XPATH, "//button[@id='remember']")
    ctn_btn = (By.XPATH, "//button[@class='inline-flex items-center justify-center gap-2 whitespace-nowrap text-sm font-medium focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 bg-primary text-white rounded primary-btn transition-all h-[40px] px-4 py-[14px] lg:min-h-[44px] w-full false']")
    heading = (By.XPATH, "//h2[@class='text-[28px] h-[38px] text-center font-satoshi-bold leading-[1.2] hidden lg:block']")

    def get_Agree_checkbox(self):
        self.click(self.agree_Checkbox)
        return self

    def get_Ctn_btn(self):
        self.click(self.ctn_btn)
        return self

    def get_Heading_text(self):
        return self.get_text(self.heading)