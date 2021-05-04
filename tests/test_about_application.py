import os
import pytest
import allure
import datetime

from tests.base_test import PrepareAboutApplicationPage


class TestCaseAboutApplication(PrepareAboutApplicationPage):

    @pytest.mark.Android
    @allure.epic("About application tests")
    @allure.feature("Version application")
    def test_version_application(self, marussia_apk_path: str, version: str) -> None:

        with allure.step("Checking version"):
            assert version == f'Версия {".".join(marussia_apk_path.split(os.sep)[-1].split("_v")[1].split(".")[:3:])}'

    @pytest.mark.Android
    @allure.epic("About application tests")
    @allure.feature("Copyright application")
    def test_copyright(self, mailru_copyright: str) -> None:

        with allure.step("Checking copyright"):
            assert mailru_copyright == f'Mail.ru Group © 1998–{datetime.date.today().year}. Все права защищены.'
