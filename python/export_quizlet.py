import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
options = Options()
options.add_argument("--headless=new")  # Start in maximized mode for visibility
options.add_argument("--disable-blink-features=AutomationControlled")  # Reduce bot detection
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")  # Mimic a real browser

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Open the Quizlet API URL
    quizlet_url = "https://quizlet.com/webapi/3.4/studiable-item-documents?filters[studiableContainerId]=906098460&filters[studiableContainerType]=1&perPage=999&page=1"
    driver.get(quizlet_url)

    # Extract response text
    response_text = driver.find_element(By.TAG_NAME, "pre").text

    # Parse the JSON data
    data = json.loads(response_text)
    print(json.dumps(data, indent=4))  # Pretty print the JSON data

finally:
    # Always quit the driver
    driver.quit()
