from web_selenium.Pages.Profile_Page import ProfilePage
import pytest
from web_selenium.Base.base import Base




@pytest.mark.usefixtures('sing_up')
class TestProfile(Base):


    def test_search_success(self):
        driver = self.driver
        profile = ProfilePage(driver)
        profile.enter_profilepage()
        profile.enter_search('simha')
        profile.enter_buttomSerch()
        self.driver.implicitly_wait(10)

        try:
            assert driver.title == "profileImage"
        except Exception as e:
            print("Title is wrong", format(e))


    def test_search_null(self):
        driver = self.driver
        profile = ProfilePage(driver)
        profile.enter_profilepage()
        profile.enter_search("")
        profile.enter_buttomSerch()
        self.driver.implicitly_wait(10)

        try:
            assert driver.title == "WeTech"
        except Exception as e:
            print("Title is wrong", format(e))

