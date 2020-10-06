import json
import requests

text_response = requests.get('https://quotes.rest/qod.json')
text = text_response.json()
print(json.dumps(text, indent=4))
q = text['contents']['quotes'][0]
print(q['quote'])