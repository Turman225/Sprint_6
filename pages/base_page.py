import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def scroll_to_the_footer(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def assert_url(self, result):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url == result)
        assert self.driver.current_url == result, (f"Проверка URL провалена \n "
                                                   f"Текущий URL = {self.driver.current_url}")

    def write_in_field(self, input=None, text=None):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(input)).send_keys(text)