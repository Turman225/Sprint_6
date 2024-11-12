import time

import pytest
import allure
import data as data
from pages.order_page import OrderPage


class TestOrderPage:

    @pytest.fixture(autouse=True)
    def setup_method(self, driver):
        self.driver = driver
        self.order_page = OrderPage(driver, data.URL)

    @pytest.mark.parametrize("button, name, second_name, address, station, phone, date, period, color, comment", [
        ('nav', 'Тестер', 'Тестович', 'К черту на куличики', 'Достоевская', '+77221321122', '01.01.2024', 'сутки', 'чёрный жемчуг', 'привезите быстрее'),
        ('center','Супер', 'Юзер', 'К Красной площади', 'Кожуховская', '+71231232222', '12.11.2024', 'пятеро суток', 'серая безысходность', 'позвоните как привезете')
    ])
    def test_ordering(self, button, name, second_name, address, station, phone, date, period, color, comment):
        self.driver.get(data.URL)
        self.order_page.click_order_button_in_nav_bar()
        self.order_page.assert_url('https://qa-scooter.praktikum-services.ru/order')
        self.order_page.fill_first_form(name, second_name, address, station, phone)
        self.order_page.fill_second_form(date, period, color, comment)

        self.order_page.click_order_button()
        time.sleep(2)
        self.order_page.click_accept_order_button()
        time.sleep(5)
