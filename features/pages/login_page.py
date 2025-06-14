from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://opensource-demo.orangehrmlive.com/'
        self.wait = WebDriverWait(driver, 10)
        self.user_name_field_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        self.password_field_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        self.login_button_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

    def open(self):
        self.driver.get(self.base_url)

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.user_name_field_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def wait_for_login_page(self):
        wait = WebDriverWait(self.driver, 120)
        return wait.until(EC.visibility_of_element_located((By.XPATH, self.login_button_xpath)))