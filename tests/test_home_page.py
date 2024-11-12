import allure
import pytest
import allure_data as test_cases
import data as data
from pages.home_page import HomePage



class TestHomePage:
    @pytest.fixture(autouse=True)
    def setup_method(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver, data.URL)

    @pytest.mark.parametrize('case, index, elem', [(test_cases.CASE_1,  0, HomePage.according_panel_element1),
                                                    (test_cases.CASE_2, 1, HomePage.according_panel_element2),
                                                    (test_cases.CASE_3, 2, HomePage.according_panel_element3),
                                                    (test_cases.CASE_4, 3, HomePage.according_panel_element4),
                                                    (test_cases.CASE_5, 4, HomePage.according_panel_element5),
                                                    (test_cases.CASE_6, 5, HomePage.according_panel_element6),
                                                    (test_cases.CASE_7, 6, HomePage.according_panel_element7),
                                                    (test_cases.CASE_8, 7, HomePage.according_panel_element8)])
    def test_accordion_ask_importan(self, case, index, elem):
        allure.dynamic.title(case['title'])
        allure.dynamic.description(case['description'])
        self.run_test_accordion(index, elem)

    def run_test_accordion(self, index, elem):
        self.driver.get(data.URL)
        self.home_page.scroll_to_the_footer()
        self.home_page.check_content_text(index, elem)