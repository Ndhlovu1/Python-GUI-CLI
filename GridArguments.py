#@Author_Socket
#Mostly used args of grid
#Find and Replace
"""
You can always use the cli to get quick help
help(tkinter.Grid)

"""

from tkinter import *
f = Tk()
f.title('Find & Replace')

Label(f, text="Find").grid(row=0, column=0, sticky='e')
Entry(f, width=60).grid(row=0, column = 1,padx=2, pady=2, sticky='we', columnspan=9)

Label(f,text="Replace:").grid(row=1, column=1, padx=2,pady=2 ,sticky='e',)
Entry(f,).grid(row=1, column=1, padx=2, pady=2, sticky='we', columnspan=9)

Button(f, text="Find").grid(row=0, column=10, sticky='e'+'w',padx=2, pady=2)
Button(f, text="Find All").grid(row=1, column=10, sticky='e'+'w', padx=2)
Button(f, text="Replace").grid(row=2, column=10, sticky='e'+'w', padx=2)
Button(f, text="Replace All").grid(row=3, column=10, sticky='e'+'w',padx=2)
Checkbutton(f, text="Match whole word only").grid(row=2, column=1, columnspan=4, sticky='w')
Checkbutton(f, text="Match Case").grid(row=3, column=1, columnspan=4, sticky='w')
Checkbutton(f, text="Wrap around").grid(row=4, column=1, columnspan=4, sticky='w')
Label(f, text="Direction:").grid(row=2, column=6, sticky='w')
Radiobutton(f, text="Direction:", value=1).grid(row=3, column=6, sticky='w')
Radiobutton(f, text="Up", value=2).grid(row=3, column=7, columnspan=2, sticky='w')



f.mainloop()













































