from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:
    output_xpath = "result-output"

    def __init__(self, driver):
        self.driver = driver

    def get_output(self):
        wait = WebDriverWait(self.driver, 60)
        output_element = wait.until(EC.visibility_of_element_located((By.XPATH, self.output_xpath)))
        return output_element.text.strip()