import time

from selenium import webdriver
import json
from credentials import USER_CHROME_DIR, cookie_path


def save_cookies():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--auto-open-devtools-for-tabs")
    options.add_argument(USER_CHROME_DIR)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.linkedin.com")
    time.sleep(5)
    cookie_json = [{cookie['name']: cookie['value']} for cookie in driver.get_cookies()]
    with open(cookie_path, 'w') as f:
        json.dump(cookie_json, f, indent=4, sort_keys=True)
    driver.save_screenshot("cookies_test.png")
    driver.quit()


if __name__ == "__main__":
    save_cookies()