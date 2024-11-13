import allure
import data

class TestOrderPage:
    nav_bar_ordering_case = {"title": 'Проверка заказа самоката через кнопку "Заказать" в навигационном меню',
             "description": 'Кнопка ЗАКАЗАТЬ, должна перенаправить на форму заполнения заказа. После заполнения первой формы,'
                            'открывается вторая форма. При прохождении всех этапов заполнения должно выйти модальное окно с '
                            'сообщением о успешной отправке заявки. Нажимаем на "Посмотреть статус" и после на логотип "ЯНДЕКС",'
                            'при нажатии на логотип, должен произойти редирект на ДЗЕН',
             }
    center_page_ordering_case = {"title": 'Проверка заказа самоката через кнопку "Заказать" в центре страницы',
               "description": 'Кнопка ЗАКАЗАТЬ, должна перенаправить на форму заполнения заказа. После заполнения первой формы,'
                              'открывается вторая форма. При прохождении всех этапов заполнения должно выйти модальное окно с '
                              'сообщением о успешной отправке заявки. Нажимаем на "Посмотреть статус" и после на логотип "Самокат",'
                              'при нажатии на логотип открывается главная страница',
               }

    @allure.title('{nav_bar_ordering_case["title"]}')
    @allure.description('{nav_bar_ordering_case["description"]}')
    def test_ordering_click_button_in_nav_bar(self, order_page):
        order_page.open_page(data.URL)
        order_page.click_order_button_in_nav_bar()
        order_page.check_url('https://qa-scooter.praktikum-services.ru/order')
        order_page.fill_first_form(data.order_data['name'][0], data.order_data['second_name'][0],
                                        data.order_data['address'][0], data.order_data['station'][0],
                                        data.order_data['phone'][0])
        order_page.fill_second_form(data.order_data['date'][0], data.order_data['period'][0],
                                         data.order_data['color'][0], data.order_data['comment'][0])
        order_page.check_order_has_been_placed()
        order_page.click_look_status_button()
        order_page.click_yandex_logo()
        order_page.switch_window()
        order_page.check_url('https://dzen.ru/?yredirect=true')

    @allure.title('{center_page_ordering_case["title"]}')
    @allure.description('{center_page_ordering_case["description"]}')
    def test_ordering_click_button_in_center_page(self, order_page):
        order_page.open_page(data.URL)
        order_page.click_order_button_in_center_page()
        order_page.check_url('https://qa-scooter.praktikum-services.ru/order')
        order_page.fill_first_form(data.order_data['name'][1], data.order_data['second_name'][1],
                                        data.order_data['address'][1], data.order_data['station'][1],
                                        data.order_data['phone'][1])
        order_page.fill_second_form(data.order_data['date'][1], data.order_data['period'][1],
                                         data.order_data['color'][1], data.order_data['comment'][1])
        order_page.check_order_has_been_placed()
        order_page.click_look_status_button()
        order_page.click_samokat_logo()
        order_page.check_url(data.URL)
