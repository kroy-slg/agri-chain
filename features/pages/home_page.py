from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://agrichain.com"
        self.home_page_ref_xpath = "//*[@id='menu-1-3a326b4']/li[1]/a"
        self.input_field_xpath = "//*[@id='input-text']"
        self.submit_button_xpath = "//*[@id='submit-btn']"

    def open(self):
        self.driver.get(self.base_url)

    def enter_input(self, text):
        self.driver.find_element(By.XPATH, self.input_field_xpath).send_keys(text)

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def wait_for_home_page(self):
        wait = WebDriverWait(self.driver, 120)
        return wait.until(EC.visibility_of_element_located((By.XPATH, self.home_page_ref_xpath)))

    def wait_for_submit_button(self):
        wait = WebDriverWait(self.driver, 30)
        return wait.until(EC.visibility_of_element_located((By.XPATH, self.submit_button_xpath)))