import allure
import pytest
import data
from pages.home_page import HomePage



class TestHomePage:
    test_cases = [
        {"title": 'Проверка раскрытия дропдауна и соответствия текста в ответе (1-й вопрос)',
         "description": 'При нажатии на стрелочку рядом с вопросом, открывается дропдаун с текстом ответа',
         "index": 0, "elem": HomePage.according_panel_element1},
        {"title": 'Проверка раскрытия дропдауна и соответствия текста в ответе (2-й вопрос)',
         "description": 'При нажатии на стрелочку рядом с вопросом, открывается дропдаун с текстом ответа',
         "index": 1, "elem": HomePage.according_panel_element2},
        {"title": 'Проверка раскрытия дропдауна и соответствия текста в ответе (3-й вопрос)',
         "description": 'При нажатии на стрелочку рядом с вопросом, открывается дропдаун с текстом ответа',
         "index": 2, "elem": HomePage.according_panel_element3},
        {"title": 'Проверка раскрытия дропдауна и соответствия текста в ответе (4-й вопрос)',
         "description": 'При нажатии на стрелочку рядом с вопросом, открывается дропдаун с текстом ответа',
         "index": 3, "elem": HomePage.according_panel_element4},
        {"title": 'Проверка раскрытия дропдауна и соответствия текста в ответе (5-й вопрос)',
         "description": 'При нажатии на стрелочку рядом с вопросом, открывается дропдаун с текстом ответа',
         "index": 4, "elem": HomePage.according_panel_element5},
        {"title": 'Проверка раскрытия дропдауна и соответствия текста в ответе (6-й вопрос)',
         "description": 'При нажатии на стрелочку рядом с вопросом, открывается дропдаун с текстом ответа',
         "index": 5, "elem": HomePage.according_panel_element6},
        {"title": 'Проверка раскрытия дропдауна и соответствия текста в ответе (7-й вопрос)',
         "description": 'При нажатии на стрелочку рядом с вопросом, открывается дропдаун с текстом ответа',
         "index": 6, "elem": HomePage.according_panel_element7},
        {"title": 'Проверка раскрытия дропдауна и соответствия текста в ответе (8-й вопрос)',
         "description": 'При нажатии на стрелочку рядом с вопросом, открывается дропдаун с текстом ответа',
         "index": 7, "elem": HomePage.according_panel_element8},
    ]

    @pytest.mark.parametrize('case', test_cases)
    @allure.title("{case[title]}")
    def test_accordion_ask_important(self, home_page, case):
        allure.dynamic.description(case['description'])
        home_page.open_page(data.URL)
        home_page.scroll_to_the_footer()
        home_page.check_content_text(case['index'], case['elem'])
