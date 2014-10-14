#!/usr/bin/python
import urllib
from xml.dom import minidom
url = 'http://detik.feedsportal.com/c/33613/f/656083/index.rss'
xmldoc = minidom.parse(urllib.urlopen(url))

itemList = xmldoc.getElementsByTagName('item')

print len(itemList)
for a in itemList :
	print a.getElementsByTagName('title')[0].childNodes[0].nodeValue
	print a.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue
	print a.getElementsByTagName('link')[0].childNodes[0].nodeValue
