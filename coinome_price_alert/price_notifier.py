# Coinome Bitcoin Price Checker
# Author : Ketan D. Ramteke
# github.com/theketan2
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

url = "https://www.coinome.com/exchange/btc-inr"
price = 0;
while True:
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    last = soup.find(attrs={"class":"last-market-rate"})
    high = soup.find(attrs={"class":"high-market-rate"})
    low = soup.find(attrs={"class":"low-market-rate"})
    avg = soup.find(attrs={"class":"market-weighted-avg"})

    last_float = float(last.span.text.encode('utf8').replace('INR ','')) # current price
    high_float = float(high.span.text.encode('utf8').replace('INR ','')) # day high
    low_float = float(low.span.text.encode('utf8').replace('INR ','')) # day low
    avg_float = float(avg.span.text.encode('utf8').replace('INR ','')) # floated average
    up = (1000) #you will get notified after price goes up or down by the value you put here.
    print up
    print last_float
    print abs(price-last_float)

    if (last_float-price)>=up:
        toaster.show_toast("Change: +"+str(round(((last_float-price)/last_float)*100,2))+"% || Change:INR "+str(abs(price-last_float)),"Current: INR "+str(last_float)+"\nHigh: INR "+str(high_float)+"\nLow: INR "+
                           str(low_float)+"\nAVG: INR "+str(avg_float),icon_path="green.ico",duration=50)
        price = last_float
    elif(price-last_float)>=(up):

        toaster.show_toast("Change: "+str(round((abs(price - last_float)/price)*100,2))+"% || Change:INR "+str(-(abs(price-last_float))),
                           "Current: INR " + str(last_float) + "\nHigh: INR " + str(high_float) + "\nLow: INR " +
                           str(low_float) + "\nAVG: INR " + str(avg_float),icon_path="red.ico", duration=50)
        price = last_float

    time.sleep(120) # program will check prices after this interval. you can change it according to your choice.