"""
print dates and the program names

"""
import requests
from bs4 import BeautifulSoup

page_response = requests.get('https://www.udacity.com/school-of-data-science')
page_text = page_response.text
soup_response = BeautifulSoup(page_text, "html5lib")


content = soup_response.find_all('ul', class_='description regular slate')
print(content)

