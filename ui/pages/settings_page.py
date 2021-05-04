import allure

from selenium.common import exceptions

from ui.pages.base_page import AndroidBasePageActions
from ui.locators.locators_android import SettingsPageLocators
from ui.locators.locators_android import SourcesNewsSettingsPageLocators
from ui.locators.locators_android import AboutApplicationLocators

from common.exceptions import UnsupportedPageException, NotCheckedSourcesNews


class SettingsPage(AndroidBasePageActions):
    locators = SettingsPageLocators()

    @allure.step("Go to: {page_name}.")
    def go_to(self, page_name: str):
        from ui.pages.main_page import MainPage

        if page_name == 'sources-news-settings':

            # Свайп до вкладки с источниками.
            self.swipe_to_element(self.locators.BUTTON_SOURCES_NEWS)

            # Перейти на вкладку с источниками новостей.
            self.click(self.locators.BUTTON_SOURCES_NEWS)

            return SourcesNewsSettingsPage(driver=self.driver, configuration=self.configuration)
        elif page_name == 'about-application-settings':

            # Свайп до вкладки с описаниями.
            self.swipe_to_element(self.locators.BUTTON_ABOUT_APP)

            # Нажимаем на кнопку.
            self.click(self.locators.BUTTON_ABOUT_APP)

            return AboutApplicationPage(driver=self.driver, configuration=self.configuration)
        elif page_name == 'main-page':

            # Перейти на главное меню.
            self.click(self.locators.BUTTON_GO_MAIN)

            return MainPage(driver=self.driver, configuration=self.configuration)
        else:
            raise UnsupportedPageException(f'Not found page "{page_name}".')


class SourcesNewsSettingsPage(SettingsPage):
    locators = SourcesNewsSettingsPageLocators()

    @allure.step("Set sources news to Vesti FM.")
    def set_news_sources_vestifm(self):

        # Нажать на элемент Вести FM
        self.click(locator=self.locators.BUTTON_SELECT_SOURCES)

    @allure.step("Checking checkbox in sources news.")
    def check_checkbox(self):
        # Проверк на появление галки рядом с данным пунктом.
        try:
            self.find_element(locator=self.locators.CHECKED_ITEM_SOURCES)
        except exceptions.TimeoutException:
            raise NotCheckedSourcesNews(f'Element not checked for "Vesti FM')

    @allure.step("Back to Settings page.")
    def go_back(self):

        # Перейти на вкладку с настройками.
        self.click(self.locators.BUTTON_SOURCES_BACK)

        return SettingsPage(driver=self.driver, configuration=self.configuration)


class AboutApplicationPage(SettingsPage):
    locators = AboutApplicationLocators()
