from selenium.webdriver.common.by import By


from pages.base_page import BasePage

class AgentDetailPage(BasePage):

    agent_Name = (By.NAME, "agency_name")
    role_In_agency = (By.NAME, "role_in_agency")
    email_Address = (By.NAME, "agency_email")
    website = (By.NAME, "agency_website")
    address = (By.NAME, "agency_address")
    rFo_Dropdown = (By.XPATH, "//button[@role='combobox' and @aria-haspopup='dialog']")
    next_Btn = (By.XPATH, "//button[@type='submit']")
    header = (By.XPATH, "//h3[contains(@class,'text-xl font-[700] tracking-[-0.4px]')]")

    def select_region(self, region):
        self.click(self.rFo_Dropdown)

        option = (
            By.XPATH, f"//div[contains(@class,'cursor-pointer') and .//span[normalize-space()='{region}']]"
        )

        self.click(option)

    def agent_Page(self, agent_Name, role_In_agency, email_Address, website, address, selected_region):

        self.enter_text(self.agent_Name, agent_Name)
        self.enter_text(self.role_In_agency,role_In_agency)
        self.enter_text(self.email_Address,email_Address)
        self.enter_text(self.website,website)
        self.enter_text(self.address,address)

        self.select_region(selected_region)

        self.click(self.next_Btn)

        return self

    def get_Heading_text(self):
        return self.get_text(self.header)