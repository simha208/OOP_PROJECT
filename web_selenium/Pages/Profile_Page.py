from selenium.webdriver.common.by import By

from web_selenium.Locators.Profile_Locators import ProfileLocators

class ProfilePage:

    def __init__(self, driver):
        self.driver = driver
        self.profilepage_txtbox_name = ProfileLocators.profilepage_txtbox_name
        self.search_txtbox_name = ProfileLocators.search_txtbox_name
        self.buttom_txtbox_name = ProfileLocators.buttom_txtbox_name

    def enter_profilepage(self):
        self.driver.find_element(By.XPATH,self.profilepage_txtbox_name).click()

    def enter_search(self, search):
        self.driver.find_element(By.XPATH,self.search_txtbox_name).clear()
        self.driver.find_element(By.XPATH,self.search_txtbox_name).send_keys(search)

    def enter_buttomSerch(self):
        self.driver.find_element(By.XPATH,self.buttom_txtbox_name).click()
