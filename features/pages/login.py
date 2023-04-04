from selenium.webdriver.common.by import By

class LoginPages:
    LOGO = (By.XPATH, "//div[@id='divLogo']//img")
    USERNAME = (By.CSS_SELECTOR, "input[placeholder='Username']")
    PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")