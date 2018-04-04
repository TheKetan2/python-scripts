#author:Ketan D.Ramteke
import requests
from bs4 import BeautifulSoup
url = "https://www.facebook.com/ketan.ramteke.794"
r = requests.get(url)
soup = BeautifulSoup(r.content)
str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
txt = unicode.join(u'\n',map(unicode,str))
print txt[(txt.find("_id=")+4):(txt.find("&"))]
