import pytest
import allure

from tests.base_test import AndroidBaseTestCase


class TestCaseCalculator(AndroidBaseTestCase):

    @pytest.mark.Android
    @allure.epic("Chat testing")
    @allure.feature("Calculator")
    @pytest.mark.parametrize(
        "query, result",
        [
            ("2+4", "6"),
            ("8-4", "4"),
            ("2*12", "24"),
            ("12/6", "2"),
            ("8+12*2", "32"),
            ("2+2*(2+2)", "10"),      # Баг Маруси.
            ("2+2(2+2)", "10"),       # Баг Маруси.
            ("2(2+2)", "8")           # Баг Маруси.
        ]
    )
    def test_calculator(self, query: str, result: str) -> None:

        # Отправить данные в текстовое поле
        self.main_page.send_query(query)

        # Проверяем существование результата на странице.
        self.main_page.exists_value_on_page(result)
