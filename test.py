# import requests
# from bs4 import BeautifulSoup
# # Disable certificate validation
# response = requests.get('https://finance.yahoo.com/quote/MYRSGD=X?p=MYRSGD=X&.tsrc=fin-srch&guccounter=1', verify=False)

# # Create a BeautifulSoup object to parse the HTML content
# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
# # # Find the HTML element that contains the desired class
# element = soup.find('span', class_='e3b14781 e59c8479')

# # Extract and print the text
# if element is not None:
#     print(element.text.strip())
# else:
#     print('Element not found.')

import requests
from bs4 import BeautifulSoup
# Send a GET request to the desired API URL
response = requests.get('https://www.xe.com/api/protected/statistics/?from=SGD&to=MYR')
data = response

# Access the JSON data
print(data)