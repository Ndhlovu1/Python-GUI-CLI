#@Author_Socket
#EVENTS AND CALLBACKS
"""
Adding Life to our programs
    1. Command Binding
e.g def myCallBack():
        #Do something when the button is clicked
        
after the  above callback is created,,,
Button(r, text="Click me", command=myCallBack)
_____________________________________________________
NB: the commnd binding is available for only a few options
NB: A callback is a function memory reference(my_callback in the previous example)
    thats called by another function (Button) which takes the first function as a parameter
"""
#Passing args to callbacks
"""
For callbacks that dont take arguments:
 def my_callback(arg)
    #do something with argument

For callbacks that take arguments:

 Button(root, text="Click", command=lambda: my_callback('some argument'))

#The lambda function lets u define a single-line, nameless function on the fly.
the e.g is below:
lambda arg: #do something with arg in a single line
lambda arg x: x**2

"""
square = lambda x: x**2
print(square(5)) #Prints 25





