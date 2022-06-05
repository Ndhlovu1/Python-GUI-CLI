#@Autho_Socket
#Tkinter geometry manager
"""
The Geometry manager in python comes in three formats!

1. pack: This is the most commonly used in the simple layouts but not ideal for complex layouts.
2. grid: Provides a table like layout! and is the most commonly used Gm
3. place: provides the best control for the absolute positioning of widgets.

The most commonly used pack methods are:
    side:(LEFT,RIGHT,TOP,BOTTOM)- they decide the alignment of the window
    fill:(X,Y,BOTH, and NONE)-they decide whether the widget can grow or not)
    expand: (BOOLEAN VALUES i.e tkinter.YES/tkinter/NO,1/0,TRUE/FALSE)
    anchor: NW, N, NE, E, SE, S, SW, W and CENTER(agree with cardinal points)
    InternalPadding:(ipadx and ipady)-inside widget padding
    ExternalPadding:(padx and pady) they both default to zero

"""
from tkinter import *
root = Tk()
f= Frame(root)
#Demooos
Label(f, text="Pack of side and fill").pack()
Button(f, text="A").pack(side=LEFT, fill=Y)
Button(f, text="B").pack(side=TOP, fill=X)
Button(f, text="C").pack(side=TOP, fill=BOTH)
f.pack()
#Demo of expand options 
Label(root, text="Pack Demo of expand").pack()
Button(root, text="I dont fill x but i expand").pack(expand=1)
Button(root, text="I feel x and expand").pack(fill=X,expand=1)
root.mainloop()





















































