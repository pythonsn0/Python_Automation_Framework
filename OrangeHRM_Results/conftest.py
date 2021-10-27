import pytest
from selenium import webdriver
from utils import utils as utils
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.ie.service import Service
from webdriver_manager.microsoft import IEDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="edge", help="Type browser name: chrome or ie or edge")


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        # driver = webdriver.Chrome(executable_path=utils.CHROME_PATH)
        chrome = Service(utils.CHROME_PATH)
        chrome.start()
        driver = webdriver.Remote(chrome.service_url)

        # chrome = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=chrome)

    elif browser == 'ie':
        # driver = webdriver.Ie(executable_path=utils.IE_PATH)

        ie = Service(utils.IE_PATH)
        ie.start()
        driver = webdriver.Remote(ie.service_url)

        # ie = Service(IEDriverManager().install())
        # driver = webdriver.Ie(service=ie)

    elif browser == 'edge':
        # driver = webdriver.Edge(executable_path=utils.EDGE_PATH)
        edge = Service(utils.EDGE_PATH)
        edge.start()
        driver = webdriver.Remote(edge.service_url)

        # edge = Service(EdgeChromiumDriverManager().install())
        # driver = webdriver.Edge(service=edge)

    elif browser == 'firefox':
        # driver = webdriver.Firefox(executable_path=utils.FIREFOX_PATH)
        firefox = Service(utils.FIREFOX_PATH)
        firefox.start()
        driver = webdriver.Remote(firefox.service_url)

        # firefox = Service(GeckoDriverManager().install())
        # driver = webdriver.Firefox(service=firefox)

    driver.get(utils.URL)
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")
