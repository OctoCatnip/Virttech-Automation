from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class ExpPage(BasePage):

    exp_Dropdown = (By.XPATH, "//button[@role='combobox' and @aria-controls]")
    num_SRA = (By.NAME, "number_of_students_recruited_annually")
    focus_Area = (By.NAME, "focus_area")
    sucess_Metrics = (By.NAME, "success_metrics")
    services_Provided = (By.CSS_SELECTOR, "#_r_12j_-form-item")
    next_Btn = (By.XPATH, "//button[@type='submit']")

    # def exp_Choose(self, value):
    #     dropdown = self.wait_for_visible(self.exp_Dropdown)
    #
    #     select = Select(dropdown)
    #     select.select_by_visible_text(value)

    def exp_Choose(self, exp_choosed):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.exp_Dropdown))
        dropdown.click()

        option = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//*[@role='option' and normalize-space()='{exp_choosed}']")
            )
        )
        option.click()

    def select_Service(self, service):

        label = (By.XPATH,  f"//label[normalize-space()='{service}']")

        label_element = self.wait_for_visible(label)
        checkbox_id = label_element.get_attribute("for")
        checkbox = (By.ID, checkbox_id)
        checkbox_element = self.wait_for_visible(checkbox)

        if checkbox_element.get_attribute("aria-checked") == "false":
            self.click(checkbox)

    def exp_page(self, num_sra, focus_area, sucess_metrics, exp_choosed, select_services):

        self.exp_Choose(exp_choosed)

        self.enter_text(self.num_SRA, num_sra)
        self.enter_text(self.focus_Area, focus_area)
        self.enter_text(self.sucess_Metrics, sucess_metrics)

        self.select_Service(select_services)

        self.click(self.next_Btn)

        return self


