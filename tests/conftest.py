import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    # Инициализация браузера
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Передача браузера в тесты
    yield driver
    # Закрытие браузера после завершения всех тестов
    driver.quit()