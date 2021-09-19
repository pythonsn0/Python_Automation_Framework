import pytest

from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import allure
import moment


@pytest.mark.usefixtures("test_setup")
class TestOrangeHRM():

    def test_login(self):

        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:

            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            # assert x == "abc"
            assert x == "OrangeHRM"
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            current_time = moment.now().strftime("%d-%m-%y_%H-%M-%S")
            function_name = utils.whoami()
            screenshot_name = function_name + "_" + current_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(utils.SCREENSHOTS_PATH + screenshot_name + ".png")
            raise
        except:
            print("There was an exception")
            current_time = moment.now().strftime("%d-%m-%y_%H-%M-%S")
            function_name = utils.whoami()
            screenshot_name = function_name + "_" + current_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(utils.SCREENSHOTS_PATH + screenshot_name + ".png")
            raise
        else:
            print("No exception occurred")
        finally:
            print("I am inside finally block")

# commands:
# python -m pytest --html=reports/report1.html --self-contained-html
# python -m pytest --alluredir=C:\Study\Python\Python_Automation_Framework\reports\allure-reports
# python -m pytest --alluredir=reports/allure-reports
# allure serve reports/allure-reports
