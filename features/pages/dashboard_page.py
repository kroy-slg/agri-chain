from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    page_ref_selector = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span"

    def get_dashboard_page(self):
        wait = WebDriverWait(self.driver, 120)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.page_ref_selector)))
        return self.driver.find_element(By.XPATH, self.page_ref_selector).text