# coding: UTF-8
import json
import urllib2
import urllib
import os
import Tkinter

clip = Tkinter.Tk().clipboard_get()  # Get Clipboard Contents
searchFor = clip + ' lyrics'
parametersEncoding = [("q", searchFor)]
key = urllib.urlencode(parametersEncoding, 0)  # Encoded parameters string

searchResults = json.load(
	urllib2.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + key))  # Results in a dictionary

if searchResults["responseStatus"] == 200:
	os.system('firefox ' + searchResults['responseData']['results'][0]['url'] + ' about:blank')
else:
	print "Error"
