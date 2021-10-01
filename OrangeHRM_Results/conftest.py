import pytest
from selenium import webdriver
from utils import utils as utils


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge", help="Type browser name: chrome or ie or edge")


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=utils.CHROME_PATH)
    elif browser == 'ie':
        driver = webdriver.Ie(executable_path=utils.IE_PATH)
    elif browser == 'edge':
        driver = webdriver.Edge(executable_path=utils.EDGE_PATH)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=utils.FIREFOX_PATH)
    driver.get(utils.URL)
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")
