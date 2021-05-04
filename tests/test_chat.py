import pytest
import allure

from tests.base_test import PreparePopulationData


class TestCaseChat(PreparePopulationData):

    @pytest.mark.Android
    @allure.epic("Chat testing")
    @allure.feature("Text from chat")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_population(self, population: None) -> None:

        # Проверка численности населения.
        with allure.step("Checking country population"):
            self.main_page.exists_fact_title_on_page('146 млн.')
