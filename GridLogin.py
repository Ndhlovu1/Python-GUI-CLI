#@Author_Socket
#The Grid Geometry manager
"""
The gm consists of cells and these cells can contain any number of widgets
and can also be aligned to prevent stickiness, using the sticky option.

The sticky option can be made via the N,S,E and W options or the NW,NE,SW, and SE,

The common args are:
1. row
2. column
3. padx
4. pady
5. rowspan
6. clumnspan


"""
from tkinter import *
r = Tk()
Label(r, text="Username").grid(row=0, sticky=W)
Label(r, text="Password").grid(row=1, sticky=W)
Entry(r).grid(row=0, column=1 ,sticky= E)
Entry(r).grid(row=1, column=1 ,sticky= E)
Button(r, text="Login").grid(row=2, column=1, sticky=E)
r.mainloop()




































