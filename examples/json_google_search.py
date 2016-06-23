# coding: UTF-8
import json
from urllib.parse import urlencode
from urllib.request import urlopen

searchFor = "wikipedia"
parametersEncoding = [("q", searchFor)]
key = urlencode(parametersEncoding, 0)  # Encoded parameters string

response = urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + key)
b = response.readlines()[0]
searchResults = json.loads(b.decode("utf-8"))  # Results in a dictionary
strSearchResults = json.dumps(searchResults, indent=4)  # String Representation of JSON

if searchResults["responseStatus"] == 200:
	for result in searchResults['responseData']['results']:
		print(result['url'])
else:
	print("Error")
