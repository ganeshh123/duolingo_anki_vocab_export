import time
import configparser
import undetected_chromedriver as uc
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DuolingoBot:
    def __init__(self):
        self.driver = self.start_driver()
        self.credentials = self.load_credentials()
        self.load_cookies()

    def start_driver(self):
        options = uc.ChromeOptions()
        options.headless = False  # Set to True for headless mode

        # Load Chrome path from config
        chrome_path = self.config.get('Chrome', 'chrome_path', fallback="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

        try:
            return uc.Chrome(options=options, browser_executable_path=chrome_path)
        except Exception as e:
            raise Exception(f"Failed to start the Chrome driver: {e}")

    def load_cookies(self):
        try:
            # First, navigate to the main Duolingo page
            self.driver.get("https://www.duolingo.com")
            time.sleep(2)  # Allow page to load


            with open("cookies.json", "r") as file:
                cookies = json.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)

            # Refresh to apply cookies
            self.driver.refresh()
            time.sleep(2)
        except Exception as e:
            raise Exception(f"Failed to load cookies: {e}")

    def navigate_to_words(self):
        try:
            self.driver.get("https://www.duolingo.com/practice-hub")
            time.sleep(10)
            self.driver.find_element(By.CSS_SELECTOR, '[src="https://d35aaqx5ub95lt.cloudfront.net/images/practiceHub/9d1604d8e8f843b492862b21a8a4e822.svg"]').click()
            time.sleep(10)
        except Exception as e:
            raise Exception(f"Navigation to words failed: {e}")

    def load_full_vocab(self):
        image_selector = '[src="https://d35aaqx5ub95lt.cloudfront.net/images/practiceHub/5d6e001cb745302aecc569f09fb7d669.svg"]' 
        while True:
            try:
                image = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, image_selector))
                )
                image.click()
            except Exception:
                print("Image no longer exists; exiting the click loop.")
                break

    def extract_words(self):
        try:
            return self.driver.find_elements(By.CSS_SELECTOR, 'li._2g-qq')
        except Exception as e:
            raise Exception(f"Failed to extract words: {e}")

    def close(self):
        self.driver.quit()



