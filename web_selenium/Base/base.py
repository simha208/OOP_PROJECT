import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get(("https://wetechsocial.herokuapp.com/login"))
        self.driver.maximize_window()


        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()

    # @pytest.fixture(autouse=True)
    # def sing_up(self):
    #     driver = self.driver
    #     login = LoginPage(driver)
    #     login.enter_email('melakubetty@gmail.com')
    #     login.enter_password('123456')
    #     login.click_login()
    #     self.driver.implicitly_wait(10)



