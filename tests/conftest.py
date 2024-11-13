import pytest
from selenium import webdriver
import data as data
from pages.home_page import HomePage
from pages.order_page import OrderPage

@pytest.fixture(scope="function")
def driver():
    # Инициализация браузера
    driver = webdriver.Firefox()
    driver.maximize_window()
    # Передача браузера в тесты
    yield driver
    # Закрытие браузера после завершения всех тестов
    driver.quit()

@pytest.fixture(scope="function")
def home_page(driver):
    # Создание объекта страницы с драйвером и URL
    page = HomePage(driver, data.URL)
    yield page

@pytest.fixture(scope="function")
def order_page(driver):
    # Создание объекта страницы с драйвером и URL
    page = OrderPage(driver, data.URL)
    yield page