import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    yandex_logo = (By.XPATH, '//a[@href="//yandex.ru"]') #Логотип Яндекс
    samokat_logo = (By.XPATH, '//a[@href="/"]') #Логотип самокат

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Нажимаем на логотип Яндекс')
    def click_yandex_logo(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.yandex_logo)).click()

    @allure.step('Нажимаем на логотип Самокат')
    def click_samokat_logo(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.samokat_logo)).click()

    #Скрол до футера
    def scroll_to_the_footer(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Переключаемся на другую вкладку
    def switch_window(self):
        tabs = self.driver.window_handles
        # Переключение на вторую вкладку
        self.driver.switch_to.window(tabs[1])

    # Ввод данных в поле
    def write_in_field(self, input=None, text=None):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(input)).send_keys(text)

    @allure.step("Проверка URL")
    def check_url(self, result):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url == result)
        assert self.driver.current_url == result, (f"Проверка URL провалена \n "
                                                   f"Текущий URL = {self.driver.current_url}")
