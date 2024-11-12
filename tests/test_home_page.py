import time
import pytest
import data as data
from pages.home_page import HomePage



class TestHomePage:
    @pytest.fixture(autouse=True)
    def setup_method(self, driver):
        self.driver = driver
        self.home_page = HomePage(driver, data.URL)

    @pytest.mark.parametrize('index, elem', [(0, HomePage.according_panel_element1),(1, HomePage.according_panel_element2),
                                             (2, HomePage.according_panel_element3),(3, HomePage.according_panel_element4),
                                             (4, HomePage.according_panel_element5),(5, HomePage.according_panel_element6),
                                             (6, HomePage.according_panel_element7),(7, HomePage.according_panel_element8)])
    def test_accordion_ask_importan(self, index, elem):
        self.driver.get(data.URL)
        self.home_page.scroll_to_the_footer()
        self.home_page.check_content_text(index, elem)