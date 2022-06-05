#@Author_Socket
#Event binding
"""
bind() is the alternative to using the command binding, its syntax is:
 widget.bind(event, handler, add=None)

"""
#e.g
from tkinter import *
r = Tk()
Label(r, text='Click at different locations in the frame below').pack()
def callback(event):
    print(dir(event))
    print("you clicked at", event.x, event.y)

frame = Frame(r, bg='yellow', width=130, height=100)
frame.bind("<Button-2>", callback)
frame.pack()



#All the useful crap is above!
r.mainloop()
































