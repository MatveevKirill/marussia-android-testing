import allure

from selenium.common import exceptions

from ui.locators.locators_android import MainPageLocators
from ui.pages.base_page import AndroidBasePageActions

from common.exceptions import NotFoundElementOnPage


class MainPage(AndroidBasePageActions):
    locators = MainPageLocators()

    @allure.step("Send query to textbox: {value}.")
    def send_query(self, value: str) -> None:
        """
        Отправить запрос в текстовое поле на главной странице.
        :param value: значение для отправки.
        :return: None
        """

        # Нажать на кнопку "Клавиатуры".
        self.click(self.locators.BUTTON_KEYBOARD)

        # Отправить данные в input.
        self.send_keys(self.locators.INPUT_TEXT, value)

        # Скрыть клавиатуру.
        self.driver.hide_keyboard()

        # Нажать на кнопку.
        self.click(self.locators.BUTTON_SUBMIT)

    @allure.step("Checking for the existence of a value on a page")
    def exists_value_on_page(self, value: str) -> None:
        try:
            self.find_element(locator=(self.locators.LABEL_DIALOG_ITEM[0],
                                       self.locators.LABEL_DIALOG_ITEM[1].format(value)),
                              timeout=3)
        except exceptions.TimeoutException:
            raise NotFoundElementOnPage(f'Value "{value}" not exists on this page.')

    @allure.step("Checking for the existence of a title on a page")
    def exists_fact_title_on_page(self, title: str) -> None:
        try:
            self.get_obj_text(
                locator=(
                    self.locators.LABEL_FACT_TITLE_TEMPLATE[0],
                    self.locators.LABEL_FACT_TITLE_TEMPLATE[1].format(title)
                )
            )
        except exceptions.TimeoutException:
            raise NotFoundElementOnPage(f'Title "{title}" not exists on this page.')

    @allure.step("Go to settings page.")
    def go_to_settings(self):
        """
        Переход на страницу настроек
        :return: SettingsPage.
        """
        from ui.pages.settings_page import SettingsPage

        # Переход на страницу настроек.
        self.click(locator=(self.locators.BUTTON_BURGER_TEMPLATE[0],
                            self.locators.BUTTON_BURGER_TEMPLATE[1].format('bottom')))

        return SettingsPage(driver=self.driver, configuration=self.configuration)
