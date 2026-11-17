from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SignPage(BasePage):

    first_Name = (By.NAME, "firstName")
    last_Name = (By.NAME, "lastName")
    email_Address = (By.NAME, "email")
    phone_Number = (By.NAME, "phoneNumber")
    password = (By.NAME, "password")
    confirm_password = (By.NAME, "confirmPassword")
    header = (By.XPATH, "//h2[@class='text-lg lg:text-2xl font-bold tracking-[-0.56px] leading-[135%] pb-2']")
    next_Btn = (By.XPATH, "//button[@type='submit']")


    def sign_Page_1(self, frist_Name, last_Name, email_Address, phone_Number, password, confirm_password):
        self.enter_text(self.first_Name, frist_Name)
        self.enter_text(self.last_Name, last_Name)
        self.enter_text(self.email_Address, email_Address)
        self.enter_text(self.phone_Number, phone_Number)
        self.enter_text(self.password, password)
        self.enter_text(self.confirm_password, confirm_password)
        self.click(self.next_Btn)
        return self

    def get_Heading_text(self):
        return self.get_text(self.header)