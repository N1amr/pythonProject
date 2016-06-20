# coding: UTF-8
import json
import urllib2
import urllib

searchFor = "wikipedia"
parametersEncoding = [("q", searchFor)]
key = urllib.urlencode(parametersEncoding, 0)  # Encoded parameters string

searchResults = json.load(
	urllib2.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + key))  # Results in a dictionary
strSearchResults = json.dumps(searchResults, indent=4)  # String Representation of JSON

if searchResults["responseStatus"] == 200:
	for result in searchResults['responseData']['results']:
		print result['url']
else:
	print "Error"
