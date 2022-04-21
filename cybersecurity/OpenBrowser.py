import webbrowser

from tkinter import *

root = Tk( ) #storing TK method

root.title('Open Browser') #title to window
root.geometry('300x200') #window size (pixels)

def googleOpen():
    webbrowser.open('www.google.com') #defining wich site

#defining button (pady=position)
mygoogle = Button(root, text='Click here to Open Google', command=googleOpen).pack(pady=20)
root.mainloop() #to call root (open window)