from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"/c:/Users/iryna/BecomeQA"
    DRIVER_NAME = "cromdriver"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )
        
    def close(self):
        self.driver.close()