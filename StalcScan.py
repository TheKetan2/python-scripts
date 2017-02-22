from Tkinter import *
import webbrowser
import requests
from bs4 import BeautifulSoup


url = ""
txt = ""

def photos_of():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/photos-by/')

def videos_of():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/videos-of/')

def stories_of():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/stories-of/')

def groups_of():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/groups')


def events_of():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/events-joined')

def past_events_of():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/events-joined/in-past/date/events/intersect/')

def games_of():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/apps-used/game/apps/intersect')

def apps_of():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/apps-used/')


def show_photos():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/photos-of/intersect')

def show_vdos():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/videos-of/intersect')

def show_stories():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/stories-tagged/intersect')
	

def show_vdos():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/videos-of/intersect')

def photo_comment():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/photos-commented/intersect')

def liked_vdos():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/videos-liked/intersect')

def liked_photos():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/photos-liked/intersect')

def liked_story():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/stories-liked/intersect')
	

def place_visited():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/places-visited/')

def bar_visited():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/places-visited/110290705711626/places/intersect/')


def restaurent_visited():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/places-visited/273819889375819/places/intersect/')


def stores_visited():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/places-visited/200600219953504/places/intersect/')

def outdoor_visited():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/places-visited/935165616516865/places/intersect/')

def hotels_visited():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/places-visited/164243073639257/places/intersect/')

def theaters_visited():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/places-visited/192511100766680/places/intersect/')

def pages_visited():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/pages-liked/intersect/')

def politics():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/pages-liked/161431733929266/pages/intersect/')

def religion():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/pages-liked/religion/pages/intersect/')

def music():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/pages-liked/musician/pages/intersect/')

def movie():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/pages-liked/movie/pages/intersect/')

def book():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/pages-liked/book/pages/intersect/')

def places():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/places-liked/')
	
def family():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/relatives/intersect/')

def friends():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/friends/intersect/')

def friend_of_friend():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/friends/friends/intersect/')

def co_worker():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/employees/intersect/')

def classmates():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/schools-attended/ever-past/intersect/students/intersect/')


def locals():
	url = e1.get()
	r = requests.get(url)
	soup = BeautifulSoup(r.content)	
	str = soup.findAll("a",{"class":"uiButton uiButtonSpecial uiButtonLarge"})
	txt = unicode.join(u'\n',map(unicode,str))
	print (txt[(txt.find("_id=")+4):(txt.find("&"))])
	#Label(master,text = txt[(txt.find("_id=")+4):(txt.find("&"))]).pack()
	webbrowser.open('https://www.facebook.com/search/'+txt[(txt.find("_id=")+4):(txt.find("&"))]+'/current-cities/residents-near/present/intersect/')



master = Tk()

#returns facebook is 

Label(master,text="FB URL: ").grid(row=0,column=1)

e1 = Entry(master).grid(row=0,column=2)



#Profiles
Label(master,text="Profiles").pack()

Button(master,text="Photos",command=photos_of).grid(row=2,column=1)

Button(master,text="Videos",command=videos_of).grid(row=2,column=2)

Button(master,text="Story",command=stories_of).grid(row=2,column=3)

Button(master,text="Groups",command=groups_of).grid(row=2,column=4)

Button(master,text="Events",command=events_of).grid(row=2,column=5)

Button(master,text="Past Events",command=past_events_of).grid(row=2,column=6)

Button(master,text="Games",command=games_of).grid(row=2,column=7)

Button(master,text="Apps",command=apps_of).grid(row=2,column=8)


#Tags
Label(master,text="Tags").grid(row=3,column=1)

Button(master,text="Photos",command=show_photos).grid(row=4,column=1)

Button(master,text="Videos",command=show_vdos).grid(row=4,column=2)

Button(master,text="Videos",command=show_stories).grid(row=4,column=3)

Label(master,text="Commented On").pack()

Button(master,text="Photos",command=photo_comment).grid(row=6,column=1)


#Liked
Label(master,text="Liked").pack()

Button(master,text="Videos",command=liked_vdos).grid(row=8,column=1)

Button(master,text="Photos",command=liked_photos).grid(row=8,column=2)


Button(master,text="Story",command=liked_story).grid(row=8,column=3)


#Places
Label(master,text="Places").pack()

Button(master,text="All",command=place_visited).grid(row=10,column=1)

Button(master,text="Bar",command=bar_visited).grid(row=10,column=2)

Button(master,text="Restarents",command=restaurent_visited).grid(row=10,column=3)

Button(master,text="Stores",command=stores_visited).grid(row=10,column=4)

Button(master,text="Outdoor",command=outdoor_visited).grid(row=10,column=5)

Button(master,text="Hotels",command=hotels_visited).grid(row=10,column=6)

Button(master,text="Theatres",command=theaters_visited).grid(row=10,column=7)


#People
Label(master,text="People").pack()

Button(master,text="Family",command=family).grid(row=12,column=1)

Button(master,text="Friends",command=friends).grid(row=12,column=2)

Button(master,text="Friends of Friends",command=friend_of_friend).grid(row=12,column=3)

Button(master,text="Co Worker",command=co_worker).grid(row=12,column=4)

Button(master,text="Classmates",command=classmates).grid(row=12,column=5)

Button(master,text="Locals",command=locals).grid(row=12,column=6)

#Interests
Label(master,text="Interests").pack()

Button(master,text="Pages",command=pages_visited).grid(row=13,column=1)

Button(master,text="Political Parties",command=politics).grid(row=13,column=2)

Button(master,text="Religion",command=religion).grid(row=13,column=3)

Button(master,text="Music",command=music).grid(row=13,column=4)

Button(master,text="Movies",command=movie).grid(row=13,column=5)

Button(master,text="Books",command=book).grid(row=13,column=6)

Button(master,text="Places",command=places).grid(row=13,column=7)


mainloop()