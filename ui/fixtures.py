import os
import pytest
import allure
from _pytest.fixtures import FixtureRequest
from appium import webdriver

from ui.capability import capability_android
from ui.pages.main_page import MainPage


@pytest.fixture(scope="session")
def marussia_apk_path(root_path: str) -> str:
    return os.path.join(root_path, 'apk', 'marussia_v1.39.1.apk')


@pytest.fixture(scope="function")
def capability(marussia_apk_path: str) -> dict:
    return capability_android(
        app_path=marussia_apk_path,
        app_package='ru.mail.search.electroscope',
        app_activity='.ui.activity.AssistantActivity',
    )


@pytest.fixture(scope="function")
def main_page(driver: webdriver.Remote, configuration: dict) -> MainPage:
    return MainPage(driver=driver, configuration=configuration)


@pytest.fixture(scope="function")
def driver(configuration: dict, capability: dict) -> webdriver.Remote:
    appium_url = configuration['appium']
    browser = webdriver.Remote(appium_url, desired_capabilities=capability)
    yield browser
    browser.quit()


@pytest.fixture(scope="function", autouse=True)
def ui_report(driver: webdriver.Remote, request: FixtureRequest, configuration: dict, test_dir: str) -> None:
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)
