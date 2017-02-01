import random
import requests
import time
from bs4 import BeautifulSoup

str1 = ""
url = "http://www.espncricinfo.com/india-v-england-2016-17/engine/match/1034829.html"
#change the value of url to the url of the live cricket match which you want to track
while True:
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	str2 = soup.find("title").text
	if(str2 != str1):
		print "******************"
		print str2
		str1 = str2
		time.sleep(random.randint(30,200))
		#sleep function is used to delay refresh rate of website.
        	
   
