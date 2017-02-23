from Tkinter import *
import webbrowser
import requests
from bs4 import BeautifulSoup


master = Tk()
master.title("Facebook Stalk Tool by K2")
#root = Tk()
#root.title("Step 1 : Enter FB URL")
url = ""
txt = ""


# get ID of USER
def get_id():
    url = e1.get()
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    str = soup.findAll("a", {"class": "uiButton uiButtonSpecial uiButtonLarge"})
    id = unicode.join(u'\n', map(unicode, str))
    show_id.config(text=("ID : "+(id[(id.find("_id=") + 4):(id.find("&"))])));
    print (id[(id.find("_id=") + 4):(id.find("&"))])
    return id[(id.find("_id=") + 4):(id.find("&"))]


# assign id to var txt
def assign_id():
    txt = str(get_id())
    print ("From assign id"+txt+" "+str(type(txt)))
    type(txt)

print ("Updated id: "+txt)

def photos_of():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/photos-by/')


def videos_of():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/videos-of/')


def stories_of():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/stories-of/')


def groups_of():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/groups')


def events_of():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/events-joined')


def past_events_of():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/events-joined/in-past/date/events/intersect/')


def games_of():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/apps-used/game/apps/intersect')


def apps_of():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/apps-used/')


def show_photos():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/photos-of/intersect')


def show_vdos():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/videos-of/intersect')


def show_stories():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/stories-tagged/intersect')


def show_vdos():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/videos-of/intersect')


def photo_comment():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/photos-commented/intersect')


def liked_vdos():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/videos-liked/intersect')


def liked_photos():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/photos-liked/intersect')


def liked_story():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/stories-liked/intersect')


def place_visited():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/places-visited/')


def bar_visited():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/places-visited/110290705711626/places/intersect/')


def restaurent_visited():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/places-visited/273819889375819/places/intersect/')


def stores_visited():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/places-visited/200600219953504/places/intersect/')


def outdoor_visited():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/places-visited/935165616516865/places/intersect/')


def hotels_visited():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/places-visited/164243073639257/places/intersect/')


def theaters_visited():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/places-visited/192511100766680/places/intersect/')


def pages_visited():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/pages-liked/intersect/')


def politics():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/pages-liked/161431733929266/pages/intersect/')


def religion():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/pages-liked/religion/pages/intersect/')


def music():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/pages-liked/musician/pages/intersect/')


def movie():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/pages-liked/movie/pages/intersect/')


def book():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/pages-liked/book/pages/intersect/')


def places():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/places-liked/')


def family():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/relatives/intersect/')


def friends():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/friends/intersect/')


def friend_of_friend():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/friends/friends/intersect/')


def co_worker():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/employees/intersect/')


def classmates():
    webbrowser.open(
        'https://www.facebook.com/search/' + str(get_id()) + '/schools-attended/ever-past/intersect/students/intersect/')


def locals():
    webbrowser.open('https://www.facebook.com/search/' + str(get_id()) + '/current-cities/residents-near/present/intersect/')




# returns facebook is

l1 = Label(master, text="FB URL: ",fg="red")
l1.grid(row=0, column=1)

e1 = Entry(master, width=60)
e1.insert(0,"Enter Profile URL Here")
e1.grid(row=0, column=2,rowspan=1,columnspan=3)

b1 = Button(master, text="Search", command=assign_id,width=15)
b1.grid(row=0, column=5)
show_id = Label(master, text="ID : ",fg="red")
show_id.grid(row=0, column=6)
# Profiles
l2 = Label(master, text="Profiles",fg="red")
l2.grid(row=1, column=1)

b2 = Button(master, text="Photos", command=photos_of,width=15)
b2.grid(row=2, column=1)

b3 = Button(master, text="Videos", command=videos_of,width=15)
b3.grid(row=2, column=2)

b4 = Button(master, text="Story", command=stories_of,width=15)
b4.grid(row=2, column=3)

b5 = Button(master, text="Groups", command=groups_of,width=15)
b5.grid(row=2, column=4)

b6 = Button(master, text="Events", command=events_of,width=15)
b6.grid(row=2, column=5)

b7 = Button(master, text="Past Events", command=past_events_of,width=15)
b7.grid(row=2, column=6)

b8 = Button(master, text="Games", command=games_of,width=15)
b8.grid(row=2, column=7)

b9 = Button(master, text="Apps", command=apps_of,width=15)
b9.grid(row=2, column=8)

# Tags
l3 = Label(master, text="Tags",fg="red")
l3.grid(row=3, column=1)

b10 = Button(master, text="Photos", command=show_photos,width=15)
b10.grid(row=4, column=1)

b11 = Button(master, text="Videos", command=show_vdos,width=15)
b11.grid(row=4, column=2)

b12 = Button(master, text="Videos", command=show_stories,width=15)
b12.grid(row=4, column=3)

# Commented On
l4 = Label(master, text="Commented On",fg="red")
l4.grid(row=5, column=1)

b13 = Button(master, text="Photos", command=photo_comment,width=15)
b13.grid(row=6, column=1)

# Liked
l5 = Label(master, text="Liked",fg="red")
l5.grid(row=7, column=1)

b14 = Button(master, text="Videos", command=liked_vdos,width=15)
b14.grid(row=8, column=1)

b15 = Button(master, text="Photos", command=liked_photos,width=15)
b15.grid(row=8, column=2)

b16 = Button(master, text="Story", command=liked_story,width=15)
b16.grid(row=8, column=3)

# Places
l5 = Label(master, text="Places",fg="red")
l5.grid(row=9, column=1)

b17 = Button(master, text="All", command=place_visited,width=15)
b17.grid(row=10, column=1)

b18 = Button(master, text="Bar", command=bar_visited,width=15)
b18.grid(row=10, column=2)

b19 = Button(master, text="Restarents", command=restaurent_visited,width=15)
b19.grid(row=10, column=3)

b20 = Button(master, text="Stores", command=stores_visited,width=15)
b20.grid(row=10, column=4)

b21 = Button(master, text="Outdoor", command=outdoor_visited,width=15)
b21.grid(row=10, column=5)

b22 = Button(master, text="Hotels", command=hotels_visited,width=15)
b22.grid(row=10, column=6)

b23 = Button(master, text="Theatres", command=theaters_visited,width=15)
b23.grid(row=10, column=7)

# People
l6 = Label(master, text="People",fg="red")
l6.grid(row=11, column=1)

b24 = Button(master, text="Family", command=family,width=15)
b24.grid(row=12, column=1)

b25 = Button(master, text="Friends", command=friends,width=15)
b25.grid(row=12, column=2)

b26 = Button(master, text="Friends of Friends", command=friend_of_friend,width=15)
b26.grid(row=12, column=3)

b27 = Button(master, text="Co Worker", command=co_worker,width=15)
b27.grid(row=12, column=4)

b28 = Button(master, text="Classmates", command=classmates,width=15)
b28.grid(row=12, column=5)

b29 = Button(master, text="Locals", command=locals,width=15)
b29.grid(row=12, column=6)

# Interests
l7 = Label(master, text="Interests",fg="red")
l7.grid(row=13, column=1)

b30 = Button(master, text="Pages", command=pages_visited,width=15)
b30.grid(row=13, column=1)

b31 = Button(master, text="Political", command=politics,width=15)
b31.grid(row=13, column=2)

b32 = Button(master, text="Religion", command=religion,width=15)
b32.grid(row=13, column=3)

b33 = Button(master, text="Music", command=music,width=15)
b33.grid(row=13, column=4)

b34 = Button(master, text="Movies", command=movie,width=15)
b34.grid(row=13, column=5)

b35 = Button(master, text="Books", command=book,width=15)
b35.grid(row=13, column=6)

b36 = Button(master, text="Places", command=places,width=15)
b36.grid(row=13, column=7)

author = Label(master,text="BY Ketan Ramteke")
author.grid(row=15,column=7)
mainloop()