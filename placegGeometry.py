#@Author_Socket
#Place Geometry
"""
place()
Uses the (x/y) co-ordinate system
lets u to precisely position the the widgets within the pareent window

The important options for place geometry(pg)
1. Absolute Position(used as x=N / y=N)
2. Relative Positioning(used as relx, rely, relwidth, and relheight)

The other options that r commonly used include the:
    width and the anchor(default is NW)
    
to get the full help check out


import tkinter
help(tkinter.place)

"""
from tkinter import *
r = Tk()
r.title("Place Geometry with place")

#ABSOLUTE P.n
Button(r, text="Absolute Placement").place(x=20, y=10)
#R.Posning
Button(r, text="Relative ").place(relx=0.4, rely=0.3, relwidth=0.5 ,width=10, anchor=NE)

r.mainloop()

















