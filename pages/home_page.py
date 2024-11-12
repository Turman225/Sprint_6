import data
import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    accordion_heading_elements = (By.XPATH, '//div[@class="accordion__heading"]/div[1]') # список вопросов
    according_panel_element1 = (By.ID, 'accordion__panel-0') #Ответ на первый вопрос
    according_panel_element2 = (By.ID, 'accordion__panel-1')#Ответ на второй вопрос
    according_panel_element3 = (By.ID, 'accordion__panel-2')#Ответ на третий вопрос
    according_panel_element4 = (By.ID, 'accordion__panel-3')#Ответ на четвертый вопрос
    according_panel_element5 = (By.ID, 'accordion__panel-4')#Ответ на пятый вопрос
    according_panel_element6 = (By.ID, 'accordion__panel-5')#Ответ на шестой вопрос
    according_panel_element7 = (By.ID, 'accordion__panel-6')#Ответ на седьмой вопрос
    according_panel_element8 = (By.ID, 'accordion__panel-7')#Ответ на восьмой вопрос
    order_button_in_nav_bar = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[1]') #Кнопка ЗАКАЗАТЬ в навигационном меню
    order_button_in_center_page = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button')#Кнопка ЗАКАЗАТЬ в центре страницы

    #Получаем список елементов аккордеона
    def get_according_heading_elem(self):
        elems = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.accordion_heading_elements))
        return elems

    # Получаем текст ответа под вопросом
    def get_content_text(self, index, answer):
        self.click_ask(index)
        text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(answer))
        return text.text

    @allure.step('Нажимаем на стрелочку около вопроса')
    def click_ask(self, index):
        self.get_according_heading_elem()[index].click()

    @allure.step('Нажимаем на кнопку ЗАКАЗАТЬ в навигационном меню')
    def click_order_button_in_nav_bar(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.order_button_in_nav_bar)).click()

    @allure.step('Нажимаем на кнопку ЗАКАЗАТЬ в центре страницы')
    def click_order_button_in_center_page(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.order_button_in_center_page))
        location = button.location
        self.driver.execute_script(f"window.scrollTo({location['x']}, {location['y']});")
        button.click()

    @allure.step("Проверяем соответствие текста ответа под выбранным вопросом")
    def check_content_text(self, index, answer):
        assert self.get_content_text(index, answer) == data.expected_content_asks[index], \
            f"{self.get_content_text(index, answer)} != {data.expected_content_asks[index]}"