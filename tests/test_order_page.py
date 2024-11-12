import pytest
import allure
import data as data
import allure_data as test_cases
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.fixture(autouse=True)
    def setup_method(self, driver):
        self.driver = driver
        self.order_page = OrderPage(driver, data.URL)

    @pytest.mark.parametrize("case, button, name, second_name, address, station, phone, date, period, color, comment", [
        (test_cases.CASE_9, 'nav', 'Тестер', 'Тестович', 'К черту на куличики', 'Черкизовская', '+77221321122', '01.01.2024', 'сутки', 'чёрный жемчуг', 'привезите быстрее'),
        (test_cases.CASE_10, 'center','Супер', 'Юзер', 'К Красной площади', 'Сокольники', '+71231232222', '12.11.2024', 'пятеро суток', 'серая безысходность', 'позвоните как привезете')
    ])

    def test_ordering(self, case, button, name, second_name, address, station, phone, date, period, color, comment):
        allure.dynamic.title(case['title'])
        allure.dynamic.description(case['description'])
        self.run_test_ordering(button, name, second_name, address, station, phone, date, period, color, comment)

    def run_test_ordering(self, button, name, second_name, address, station, phone, date, period, color, comment):
        self.driver.get(data.URL)
        if button == 'nav':
            self.order_page.click_order_button_in_nav_bar()
        else:
            self.order_page.click_order_button_in_center_page()
        self.order_page.check_url('https://qa-scooter.praktikum-services.ru/order')
        self.order_page.fill_first_form(name, second_name, address, station, phone)
        self.order_page.fill_second_form(date, period, color, comment)
        self.order_page.check_order_has_been_placed()
        self.order_page.click_look_status_button()
        if button == 'nav':
            self.order_page.click_yandex_logo()
            self.order_page.switch_window()
            self.order_page.check_url('https://dzen.ru/?yredirect=true')
        else:
            self.order_page.click_samokat_logo()
            self.order_page.check_url(data.URL)