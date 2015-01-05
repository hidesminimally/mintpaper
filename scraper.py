from lxml import html
import requests 
import urllib2
url = 'http://www.reddit.com/r/spaceporn'
request = urllib2.Request(url)
request.add_header('User-Agent', 'Mozilla 3.10')

page = requests.get(url)
tree = html.fromstring(page.text)

image = tree.xpath('//p[@class="title"]/a/@href')
print image
