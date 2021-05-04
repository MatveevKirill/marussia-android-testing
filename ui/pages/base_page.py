import allure
import logging
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement

from utils.decoders import wait

from common.exceptions import InvalidLogLevelException, UndefinedSwipeType


class AndroidBasePageActions(object):
    locators = None

    driver: webdriver.Remote = None
    configuration: dict = None

    def __init__(self, driver: webdriver.Remote, configuration: dict) -> None:
        self.driver = driver
        self.configuration = configuration

    @property
    def touch_action(self) -> TouchAction:
        return TouchAction(self.driver)

    def _wait(self, timeout: float = None) -> WebDriverWait:
        if timeout is None:
            timeout = self.configuration['timeout_limit']

        return WebDriverWait(driver=self.driver, timeout=timeout)

    def find_element(self, locator: tuple, timeout: float = None) -> WebElement:
        if timeout is None:
            timeout = self.configuration['timeout_limit']
        return self._wait(timeout=timeout).until(EC.presence_of_element_located(locator=locator))

    def click(self, locator: tuple, timeout: float = None) -> None:

        def _click():
            self.find_element(locator=locator, timeout=timeout).click()

        with allure.step("Click on element '{locator}' with timeout '{timeout}'."):
            return wait(
                _method=_click,
                _error=exceptions.StaleElementReferenceException,
                _timeout=self.configuration['timeout_limit']
            )

    def get_obj_text(self, locator: tuple, timeout: float = None) -> str:

        def _get_obj_text():
            return self.find_element(locator=locator, timeout=timeout).text

        return wait(
            _method=_get_obj_text,
            _error=exceptions.StaleElementReferenceException,
            _timeout=self.configuration['timeout_limit']
        )

    def send_keys(self, locator: tuple, value: str, timeout: float = None, auto_clear: bool = True) -> None:
        if timeout is None:
            timeout = self.configuration['timeout_limit']

        def _send_keys():
            element = self.find_element(locator=locator, timeout=timeout)
            if auto_clear:
                element.clear()
            element.send_keys(value)

        return wait(
            _method=_send_keys,
            _error=exceptions.StaleElementReferenceException,
            _timeout=timeout
        )

    def _swipe_on_screen(
            self,
            locator: tuple = None,
            swipe_max: int = 10,
            swipe_type: str = 'down',
            timeout: float = None
    ) -> None:

        def _touch_action(start_x: int, end_x: int, start_y: int, end_y: int, ms: int = 200) -> None:
            self.touch_action. \
                press(x=start_x, y=start_y). \
                wait(ms=ms). \
                move_to(x=end_x, y=end_y). \
                release(). \
                perform()

        def _swipe_to(k_start: float, k_end: float) -> None:
            size = self.driver.get_window_size()

            x = int(size['width'] / 2)
            start_y = int(size['height'] * k_start)
            end_y = int(size['height'] * k_end)

            _touch_action(x, x, start_y, end_y)

        if swipe_type == 'up':

            # Переместить экран вверх.
            _swipe_to(0.4, 0.6)

        elif swipe_type == 'down':

            # Переместить экран вниз.
            _swipe_to(0.6, 0.4)

        elif swipe_type == 'to_element':

            # Переместить экран к элементу.
            count_swipes = 0
            while len(self.driver.find_elements(*locator)) == 0:
                if count_swipes > swipe_max:
                    raise exceptions.TimeoutException(f'Unable to navigate to element: {locator}.')
                self._swipe_on_screen()
                count_swipes += 1

        elif swipe_type == 'middle':

            # Переместить элемент в центр.
            element = self.find_element(locator=locator, timeout=timeout)

            start_x = element.rect['x']

            upper_y = element.rect['y']
            lower_y = upper_y + element.rect['height']
            middle_y = (upper_y + lower_y) / 2

            middle_device_width = self.driver.get_window_size()['width'] / 2

            _touch_action(
                start_x,
                middle_device_width,
                middle_y,
                middle_y
            )

        else:
            raise UndefinedSwipeType(f'Got type: {swipe_type}. Expected: up, down, to_element, middle.')

    @allure.step("Swipe to element '{locator}'. Max swipes: {swipe_max}.")
    def swipe_to_element(self, locator: tuple, swipe_max: int = 7) -> None:
        self._swipe_on_screen(locator=locator, swipe_max=swipe_max, swipe_type='to_element')

    @allure.step("Swipe to {side_type} side. Max swipes: {swipe_max}.")
    def swipe_to_side(self, locator: tuple, side_type: str, swipe_max: int = 10, timeout: float = None) -> None:
        self._swipe_on_screen(locator=locator, swipe_type=side_type, swipe_max=swipe_max, timeout=timeout)
