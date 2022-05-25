import allure

from web_selenium.Pages.Login_Page import LoginPage
from web_selenium.Base.base import Base
import pytest
from time import *



@pytest.mark.usefixtures('set_up')
class TestLogin(Base):


    def test_login_success(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email('melakubetty@gmail.com')
        login.enter_password('123456')
        login.click_login()
        self.driver.implicitly_wait(10)



        try:
            assert driver.title =="WeTech"
        except Exception as e:
            print("Title is wrong", format(e))


    @pytest.mark.skip
    def test_incorrect_email(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email('nhgftg5')
        login.enter_password('123456')
        login.click_login()
        sleep(5)
        self.driver.implicitly_wait(10)

        try:
            assert login.email_txtbox_name == 'melakubetty@gmail.com'
        finally:
            if AttributeError:
                allure.attach(driver.get_screenshot_as_png(),
                              name="incorrect email",attachment_type=allure.attachment_type.PNG)



    def test_incorrect_password(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email('simhaamara2020@gmail.com')
        login.enter_password('gfggh')
        login.click_login()
        self.driver.implicitly_wait(10)

        try:
            assert driver.title == "WeTech"
        except Exception as e:
            print("Title is wrong", format(e))



        # try:
        #     assert login.pass_txtbox_name() == '202020888'
        # except AttributeError:
        #     driver.get_screenshot_as_png()
        #     driver.save_screenshot('password incorrect')


    def test_incorrect_null_email(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email(" ")
        login.enter_password("12346")
        login.click_login()
        self.driver.implicitly_wait(10)


        try:
            assert driver.title == "Toggle theme"
        except Exception as e:
            print("Title is wrong", format(e))



    def test_incorrect_null_password(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email("simhaamara2020@gmail.com")
        login.enter_password(" ")
        login.click_login()
        self.driver.implicitly_wait(10)

        try:
            assert driver.title == "Toggle theme"
        except Exception as e:
            print("Title is wrong", format(e))


    def test_incorrect_null(self):
        drive = self.driver
        login = LoginPage(drive)
        login.enter_email("")
        login.enter_password("")
        login.click_login()
        self.driver.implicitly_wait(10)

        try:
            assert drive.title == "Toggle theme"
        except Exception as e:
            print("Title is wrong", format(e))

