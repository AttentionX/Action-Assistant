from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class customDriver:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    def getLink(self, link):
        return self.driver.get(link)
    def click_offset(self, x_offset, y_offset):
        ac = ActionChains(self.driver)
        ac.move_to_element_with_offset(self.driver.find_element_by_tag_name('body'), 0,0)
        ac.move_by_offset(x_offset, y_offset).click().perform()
    def takeScreenshot(self, website_link, datetime_string):
        filename = f"{website_link}_{datetime_string}.png"
        self.driver.save_screenshot(f"./data/{filename}")
        return filename

