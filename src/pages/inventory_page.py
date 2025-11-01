from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class InventoryPage(BasePage):
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")

    def is_loaded(self):
        return self.is_visible(self.MENU_BUTTON)
