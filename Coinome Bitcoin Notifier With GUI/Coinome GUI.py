# Coinome Bitcoin Price Checker
# Author : Ketan D. Ramteke
# github.com/theketan2

import requests
from bs4 import BeautifulSoup
import time
from win10toast import ToastNotifier
import Tkinter as tk
import matplotlib.pyplot as plt
import tkMessageBox
import numpy as np
import winsound
import webbrowser

top = tk.Tk()
top.title("Coinome Bitcoin Rate Notifier")
top.geometry("600x200")
top.iconbitmap('Bitcoin.ico')

refreshRate = tk.Label(top, text="Enter Refresh Interval: \t")
refreshRate.grid(row=0, column=0, pady=5)

interval = tk.Entry(top, text="5",bd=2)
interval.grid(row=0, column=1, pady=5)

defaultMsg = tk.Label(top, text="Minutes")
defaultMsg.grid(row=0, column=2,sticky='w')

mktVolume = tk.Label(top, text="Volume Loading...")
mktVolume.grid(row=0, column=3)

price = tk.Label(top, text="Bitcoin Rate")
price.grid(row=1, column=0)

buyStaus = tk.IntVar()
buyNotify = tk.Checkbutton(top, text="Buy Notification", variable=buyStaus,
                           onvalue=1, offvalue=0)
buyNotify.grid(row=1, column=1, columnspan=1)

sellStatus = tk.IntVar()

sellNotify = tk.Checkbutton(top, text="Sell Notification", variable=sellStatus,
                            onvalue=1, offvalue=0)
sellNotify.grid(row=1, column=2, columnspan=1)

price = tk.Label(top, text="Loading...")
price.grid(row=3, column=0)
sell = tk.Entry(top, bd=2)
sell.insert(0, "Enter Sell Price")
sell.grid(row=3, column=1, pady=5)

buy = tk.Entry(top, bd=2)
buy.insert(0, "Enter Buy Price")
buy.grid(row=3, column=2, pady=5)

def plotGraph():
    f = open('bitcoin_rate.txt','r')
    historicalPrices = f.readlines()
    print type(''.join(historicalPrices))
    print (''.join(historicalPrices))

    rateArray = np.asarray(historicalPrices)
    print type(str.split(''.join(historicalPrices),','))

    plt.plot(str.split(''.join(historicalPrices),','))
    plt.title("Bitcoin Historical Price")
    plt.ylabel("Price")
    plt.xlabel("Time")
    plt.show()


chartBtn = tk.Button(top, command=plotGraph)
chartPic = tk.PhotoImage(file="graph.gif")
chartBtn.config(image=chartPic, width="116", height="20")
chartBtn.grid(row=3, column=3, pady=5)

btc = "https://www.coinome.com/exchange/btc-inr"
f = open('bitcoin_rate.txt','r')
old_price_Rip = str.split(''.join(f.readlines()),',')
print old_price_Rip[-1]
oldPrice = float(old_price_Rip[-1])
print type(oldPrice)
def startMonitering():
    global oldPrice
    r = requests.get(btc)
    soup = BeautifulSoup(r.content, "lxml")
    last = soup.find(attrs={"class": "last-market-rate"})
    volume = soup.find(attrs={"class": "market-volume"})
    rate = float(last.span.text.encode('utf8').replace('INR ', ''))  # day high
    mktVolume.config(text= volume.span.text.encode('utf8'))
    print buy.get()
    print sell.get()
    if rate > oldPrice:
        price.config(text=str(rate), bg="green")
    elif rate < oldPrice:
        price.config(text=str(rate), bg="red")
    else:
        price.config(text=str(rate))

    sellInput = sell.get()
    print type(sellInput)

    buyInput = buy.get()
    print type(buyInput)

    if sellStatus.get() == 1 and len(sellInput) != 0 and str.isdigit(sellInput) and rate >= float(sellInput) :
        winsound.PlaySound('ting.waw', winsound.SND_FILENAME)
        tkMessageBox.showinfo("Want To Sell?",str(rate))

    elif buyStaus.get() == 1 and len(buyInput) != 0 and str.isdigit(buyInput) and rate <= float(buyInput) :
        winsound.PlaySound('ting.waw', winsound.SND_FILENAME)
        tkMessageBox.showinfo("Want To Buy?",str(rate))


    print rate
    print "hello"
    oldPrice = rate
    f = open('bitcoin_rate.txt', 'a')
    f.write(',' + str(rate))
    f.close()

def monitor():

    sleepTimer = 60000
    userInterval = interval.get()
    if len(userInterval) == 0:
        sleepTimer = 60000*5
    else:
        sleepTimer = sleepTimer * int(userInterval)
    startMonitering()
    top.after(sleepTimer,monitor)


startBtn = tk.Button(top, command=monitor)
startPic = tk.PhotoImage(file="start.gif")
startBtn.config(image=startPic)
startBtn.grid(row=5, column=2, pady=5)

def callback(event):
    webbrowser.open_new("http://www.github.com/theketan2")

link = tk.Label(top, text="By: Ketan Ramteke", fg="blue", cursor="hand2")
link.grid(row=6,column=0)
link.bind("<Button-1>", callback)

top.mainloop()
