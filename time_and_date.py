import requests
from bs4 import BeautifulSoup
url = "https://www.timeanddate.com/worldclock/"
def capital():
    while True:
        country = raw_input("Enter Country: ")
        r = requests.get(url+country)
        soup = BeautifulSoup(r.content)
        capital = soup.find("div",{"class":"five columns"}).text
        clock = soup.find("span",{"class":"h1"}).text
        print(capital[capital.find("Capital"):capital.find("Time Zones")])
        print("Time:"+clock)