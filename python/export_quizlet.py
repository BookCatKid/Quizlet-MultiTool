import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def setup_webdriver():
    """
    Set up a headless Chrome WebDriver.

    Returns:
        webdriver.Chrome: The set up WebDriver.
    """
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

    return webdriver.Chrome(options=options)


def fetch_quizlet_data(url, driver):
    """
    Fetch Quizlet data from a given URL.

    Args:
        url (str): The URL of the Quizlet data to fetch.
        driver (webdriver.Chrome): The WebDriver to use for fetching the data.

    Returns:
        dict: The fetched Quizlet data as a JSON object.
    """
    if url.startswith("https://quizlet.com/webapi/3.4/studiable-item-documents"):
        url = url
    elif url.startswith("https://quizlet.com/"):
        url = f"https://quizlet.com/webapi/3.4/studiable-item-documents?filters[studiableContainerId]={url.split('/')[-3]}&filters[studiableContainerType]=1&perPage=999&page=1"
    elif url.isdigit():
        url = f"https://quizlet.com/webapi/3.4/studiable-item-documents?filters[studiableContainerId]={url}&filters[studiableContainerType]=1&perPage=999&page=1"
    else:
        raise ValueError("Invalid URL. Please provide a valid Quizlet URL.")

    driver.get(url)
    response_text = driver.find_element(By.TAG_NAME, "pre").text
    json_text = json.loads(response_text)
    return json_text


def main():
    """
    Main function to fetch and print the Quizlet data.
    """
    quizlet_url = (
        "527298863"
    )
    driver = setup_webdriver()
    try:
        data = fetch_quizlet_data(quizlet_url, driver)
        print(json.dumps(data, indent=4))
        with open("../examples/output_sample_1.json", "w") as f:
            json.dump(data, f, indent=4)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
