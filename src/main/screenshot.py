from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def capture_screenshot(url, save_path, headless=False):
    chrome_options = Options()

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1080")
    else:
        chrome_options.add_argument("--start-maximized")

    # Ensure directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Use system chromedriver if inside Docker
    if os.path.exists("/usr/bin/chromedriver"):
        service = Service("/usr/bin/chromedriver")
    else:
        service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    time.sleep(3)

    driver.save_screenshot(save_path)
    driver.quit()
