
import requests

page_response = requests.get('https://www.udacity.com/school-of-data-science')
page_text = page_response.text
print(page_text)
