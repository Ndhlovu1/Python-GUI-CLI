#@Author_Socket
#Remember Widget
#NB: THIS CODE ISNT THE FULL CODE THAT CAN RUN!
from tkinter import *
f = Tk()
pwd = Label(f, text="Enter your Password")
pwd.pack()
sch = Button(f, text="SEARCH")
sch.pack()
cbtn = Checkbutton(f, text="REMEMBER ME", variable=v, value=True)
cbtn.pack()
kb = Entry(f, width=30)
kb.pack()
rbtn = Radiobutton(f, text="Male", variable=v, value=1)
rbtn.pack()
rbtn2 = Radiobutton(f, text="Frmale", variable=v, value=2)
rbtn2.pack()
om = Optionmenu(f, var, "Select Country", "Zim", "Nam", "Others")
om.pack()
sb = Scrollbar(f, orient=VERTICAL, command = text.yview)


#All code miust be above this 
f.mainloop()




















