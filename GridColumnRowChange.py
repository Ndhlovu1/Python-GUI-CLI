#@Author_Socket
#Overriding the automatic sizing of rows and columns
"""
w.columnconfigure(n, option=value, ...) AND
w.rowconfigure(N, option=value, ...)
w=widget
n = nth column or nth row, specifying values for the options:
    1. minisize- the minimum size of a column or row in pixels, if there's no widget in the cell
    this specification wont appear even if its mentioned
    2. pad: This is the external paddingin pixels that will be added to the specified column or row
            over the largest cell.
    3. weight: This specifies the weight of a row/column then distributes the extra space. This enables
               the row/column to be stretchable.
    e.g w.config(0, weight=2)
        w.configure(1, weight=3)
               
THE columnconfig() and the rowconfig() methods are often used to perform the dynamic resizing of widgets especially the root window


"""









