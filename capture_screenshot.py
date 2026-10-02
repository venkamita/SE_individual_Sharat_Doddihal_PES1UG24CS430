import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

html_path = "file:///" + os.path.abspath("copilot_mock.html").replace("\\", "/")

options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=850,700')

try:
    driver = webdriver.Chrome(options=options)
    driver.get(html_path)
    # allow time for rendering
    time.sleep(2)
    # Take screenshot of the editor container
    element = driver.find_element("css selector", ".editor-container")
    element.screenshot("5-GitHub_Copilot_Code/copilot_screenshot_01.png")
    driver.quit()
    print("Screenshot saved to 5-GitHub_Copilot_Code/copilot_screenshot_01.png")
except Exception as e:
    print("Error taking screenshot:", e)
