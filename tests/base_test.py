import pytest

from appium import webdriver
from _pytest.fixtures import FixtureRequest

from ui.pages.main_page import MainPage
from ui.pages.settings_page import AboutApplicationPage, SettingsPage, SourcesNewsSettingsPage


class AndroidBaseTestCase(object):
    main_page: MainPage = None

    driver: webdriver.Remote = None
    configuration: dict = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver: webdriver.Remote, configuration: dict, request: FixtureRequest) -> None:
        self.driver = driver
        self.configuration = configuration

        self.main_page = request.getfixturevalue('main_page')


class PrepareAboutApplicationPage(AndroidBaseTestCase):

    @pytest.fixture(scope="function")
    def about_page(self) -> AboutApplicationPage:
        settings: SettingsPage = self.main_page.go_to_settings()
        yield settings.go_to('about-application-settings')

    @pytest.fixture(scope="function")
    def version(self, about_page: AboutApplicationPage) -> str:
        yield about_page.get_obj_text(locator=about_page.locators.LABEL_APPLICATION_VERSION)

    @pytest.fixture(scope="function")
    def mailru_copyright(self, about_page: AboutApplicationPage) -> str:
        yield about_page.get_obj_text(locator=about_page.locators.LABEL_COPYRIGHT)


class PreparePopulationData(AndroidBaseTestCase):

    @pytest.fixture(scope="function")
    def population(self) -> None:

        # Отправить данные в текстовое поле.
        self.main_page.send_query('Russia')

        # Проверить название страны.
        self.main_page.exists_fact_title_on_page('Россия')

        # Свайп элемента влево.
        self.main_page.swipe_to_side(self.main_page.locators.BUTTON_POPULATION, 'middle')

        # Нажать на кнопку численности населения.
        self.main_page.click(locator=self.main_page.locators.BUTTON_POPULATION)


class PrepareNewsPage(AndroidBaseTestCase):

    @pytest.fixture(scope="function")
    def sources_news(self) -> SourcesNewsSettingsPage:

        # Перейти на страницу с настройками.
        settings: SettingsPage = self.main_page.go_to_settings()

        # Перейти на страницу с источниками
        sources: SourcesNewsSettingsPage = settings.go_to('sources-news-settings')

        # Установить настройки новостей.
        sources.set_news_sources_vestifm()

        yield sources
