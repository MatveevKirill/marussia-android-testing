import sys
import shutil
from _pytest.fixtures import Parser, Config

from ui.fixtures import *

from common.system import *


def pytest_addoption(parser: Parser) -> None:
    parser.addoption('--appium', default='http://127.0.0.1:4723/wd/hub')
    parser.addoption('--timeout-limit', default=5)


def pytest_configure(config: Config) -> None:
    base_test_dir = os.path.join(os.path.abspath(os.path.curdir), 'tmp', 'tests')

    if not hasattr(config, 'workerinput'):
        if os.path.exists(base_test_dir):
            shutil.rmtree(base_test_dir)
        os.makedirs(base_test_dir)

    config.base_test_dir = base_test_dir


@pytest.fixture(scope="session")
def configuration(request: FixtureRequest) -> dict:
    appium = request.config.getoption("--appium")
    timeout_limit = float(request.config.getoption('--timeout-limit'))

    return {
        'appium': appium,
        'timeout_limit': timeout_limit
    }


@pytest.fixture(scope="session")
def root_path() -> str:
    return os.path.abspath(os.path.join(__file__, os.pardir))


@pytest.fixture(scope="function")
def test_dir(request: FixtureRequest, root_path: str, configuration: dict) -> str:
    test_name = request._pyfuncitem.nodeid

    # Удаление запрещенных символов в строке.
    if sys.platform.startswith('win'):
        for replace_obj in SYSTEM_DISALLOW_CHARS['WINDOWS']:
            test_name = str(test_name).replace(replace_obj['char'], replace_obj['replace'])

    test_dir = os.path.join(request.config.base_test_dir, test_name)
    os.makedirs(test_dir)

    yield test_dir

    # Если файлов в директории нет, то удаляем её.
    if len([name for name in os.listdir(test_dir) if os.path.isfile(name)]) == 0:
        shutil.rmtree(test_dir)