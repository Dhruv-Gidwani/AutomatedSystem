
![image](https://github.com/user-attachments/assets/e291e823-38b4-4c1b-af9f-fbfb5ea33a67)



This project is a web scraping tool built with Python that automates the extraction of Importer/Exporter Code (IEC) details from the DGFT website. It uses Selenium for browser automation and BeautifulSoup for parsing the HTML content.

FEATURES
1. Automates the process of navigating to the IEC information page.
2. Fills out required fields, including IEC number and firm name.
3. Handles CAPTCHA input manually.
4. Extracts various IEC-related details such as:
    IEC Number
    PAN Number
    Date of Birth/Incorporation
    IEC Issuance Date
    IEC Status
    and more
5. Outputs the extracted data in a structured tabular format using pandas.


REQUIREMENTS
1. Python 3.x
2. Selenium
3. BeautifulSoup
4. pandas
5. ChromeDriver


USAGE
1. Update the ChromeDriver path in the code.
2. Run the script and follow the prompts.
3. Enter the CAPTCHA code as displayed on the screen.


DISCLAMER
Ensure you have permission to scrape the website and comply with its terms of service.
