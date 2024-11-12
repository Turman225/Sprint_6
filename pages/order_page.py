import allure
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(HomePage):

    name_input = (By.XPATH, '//input[@placeholder="* Имя"]')
    second_name_input = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    address_input = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    station_input = (By.XPATH, '//div[@class="select-search__value"]')
    phone_input = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    next_button = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    date_input = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    selected_date = (By.XPATH, '//div[@class="react-datepicker__week"]/div[@tabindex="0"]')
    period_button = (By.XPATH, '//div[@class="Dropdown-control"]')
    comment_input = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    order_button = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[2]')
    accept_order_button = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]/div[2]/button[2]')
    status_text = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')


    def get_status_text(self):
        text = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.status_text))
        return text.text

    def click_station_input(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.station_input)).click()

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.next_button)).click()

    def click_order_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.order_button)).click()

    def click_selected_date(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.selected_date)).click()

    def click_period_list(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.period_button)).click()

    def click_accept_order_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.accept_order_button)).click()

    @allure.step("Заполняем поля в форме 'Для кого самокат' данными")
    def fill_first_form(self, name=None, second_name=None, address=None, station=None, phone=None):
        if name is not None:
            self.write_in_field(self.name_input, name)
        if second_name is not None:
            self.write_in_field(self.second_name_input, second_name)
        if address is not None:
            self.write_in_field(self.address_input, address)
        if station is not None:
            self.select_station(station)
        if phone is not None:
            self.write_in_field(self.phone_input, phone)
        self.click_next_button()

    @allure.step("Заполняем поля в форме 'Про аренду' данными")
    def fill_second_form(self, date=None, period=None, color=None, comment=None):
        if date is not None:
            self.write_in_field(self.date_input, date)
            self.click_selected_date()
        if period is not None:
            self.select_rental_period(period)
        if color is not None:
            self.select_color(color)
        if comment is not None:
            self.write_in_field(self.comment_input, comment)

    @allure.step("Выбираем станцию")
    def select_station(self, station):
        self.click_station_input()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[contains(text(), "{station}")]'))).click()

    @allure.step("Выбираем срок аренды")
    def select_rental_period(self, priod):
        self.click_period_list()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//div[contains(text(), "{priod}")]'))).click()

    def select_color(self, color):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[contains(text(), "{color}")]'))).click()

    def check_order_has_been_placed(self):
        assert 'Заказ оформлен' in self.get_status_text(), f'{self.get_status_text()}'
