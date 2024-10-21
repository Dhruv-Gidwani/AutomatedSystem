from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import pandas as pd

path = 'C:/Users/dhruv/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'

service = Service(path)
driver = webdriver.Chrome(service=service)

website = 'https://www.dgft.gov.in/CP/?opt=view-any-ice'
driver.get(website)

try:
    
    view_iec_card = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'View Any IEC')]/ancestor::div[contains(@class, 'card')]"))
    )
    view_iec_card.click()
    print("Clicked on 'View Any IEC' card.")
except Exception as e:
    print("Error finding or clicking the card:", e)



try:
    
    eic_id = view_iec_card.find_element(By.XPATH, "//input[@placeholder='Enter Importer/Exporter Code']")  
    eic_id.send_keys("1210001322")

    firm_name = view_iec_card.find_element(By.XPATH, "//input[@placeholder='Enter Firm Name']")  
    firm_name.send_keys("set")
    
    captcha_field = driver.find_element(By.XPATH, "//input[@placeholder='Please enter above CAPTCHA Code']")  
    captcha_code = input("Please enter the CAPTCHA code displayed on the screen: ")  
    captcha_field.send_keys(captcha_code)

    # Click the submit button
    submit_button = view_iec_card.find_element(By.XPATH, "//button[contains(text(), 'View IEC')]")  
    submit_button.click()
    
    print("Successfully submitted the form!")

    time.sleep(10)

    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')

    def extract_detail(label):
        label_element = soup.find(string=lambda text: label in text)
        if label_element:
            value = label_element.find_next().text.strip()
            if label == "Address":
                value = ' '.join(value.split())  
            return value
        return None

    labels = [
        "IEC Number",
        "PAN Number",
        "Date of Birth / Incorporation",
        "IEC Issuance Date",
        "IEC Status",
        "DEL Status",
        "IEC Cancelled Date",
        "IEC Suspended Date",
        "File Number",
        "File Date",
        "DGFT RA Office",
        "Nature of concern/Firm",
        "Category of Exporters",
        "Firm Name",
        "Address"
    ]

    extracted_details = {}
    for label in labels:
        value = extract_detail(label)
        extracted_details[label] = value if value else "Not found"

    df = pd.DataFrame(list(extracted_details.items()), columns=['Label', 'Value'])
    print("\nExtracted Data:")
    print(df)

except Exception as e:
    print(f"An error occurred: {e}")

driver.quit()



