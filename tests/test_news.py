import pytest
import allure

from ui.pages.settings_page import SourcesNewsSettingsPage

from tests.base_test import PrepareNewsPage


class TestCaseValidateCheckbox(PrepareNewsPage):

    @pytest.mark.Android
    @allure.epic("News tests")
    def test_validate_source_news(self, sources_news: SourcesNewsSettingsPage) -> None:

        # Проверка на появление галки рядом с пунктом 'Вести ФМ'.
        sources_news.check_checkbox()

        # Вернуться на главную страницу.
        sources_news.\
            go_back().\
            go_to('main-page')

        # Отобразить данные о новостях.
        self.main_page.send_query("News")

        # Свайп до элемента.
        self.main_page.swipe_to_element(self.main_page.locators.LABEL_PLAYED_NAME)

        # Проверить новости с "Вести ФМ".
        with allure.step("Check Vesti FM"):
            assert self.main_page.get_obj_text(self.main_page.locators.LABEL_PLAYED_NAME) == "Вести ФМ"
