from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import re
import json




# Configure the Selenium webdriver
chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# options.add_argument('--headless')  # Run Chrome in headless mode, remove this line to see the browser
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
# Load the webpage
df = pd.read_csv("link.csv")
yahoo_lists = []
for index, row in df.iterrows():
    yahoo = row["Yahoo"]
    driver.get(yahoo)
    # Find the HTML element that contains the desired class
    element = driver.find_elements(By.XPATH , '//fin-streamer')[-5]
    yahoo_lists.append(element.text)
yahoo_lists = [float(num.replace(',', '')) for num in yahoo_lists]
df['Yahoo_Rate'] = yahoo_lists
df = df[["From", "To", "Yahoo_Rate"]]
df.to_csv("exchange.csv", index=False)
df.to_excel("exchange.xlsx", index=False)


# driver.quit()
# # Find JSON data using regex
# pattern = r'"5q0Os46sTrMffELfksN8Bc":({.*?})'
# json_data_match = re.search(pattern, html_source, re.DOTALL)

# if json_data_match:
#     json_string = json_data_match.group(1)
#     json_data = json.loads(json_string)
#     print(json_data)
# else:
#     print("JSON data not found.")
# print(html_source)