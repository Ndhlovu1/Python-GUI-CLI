#@Author_Socket
#Take up ur shape when the world isnt looking
#Event Patterns
"""
the <Button-1> event accepts the left click.
The event pattern                 The associated event
<Button-1>                        LEFT-Click of the mouse
<keyPress-B>                      A KB PRESS OF Letter B
<Alt-Control-KeyPress- KP_Delete> Kb press of Alt + Crtl + Delete

the pattern takes the following form:
 <[event modifier-]...event type [-event detail]>



Event pattern will alwys have an event type such as:

Activate

Destroy

Map

ButtonPress, Button

Enter

MapRequest

ButtonRelease

Expose

Motion

Circulate

FocusIn

MouseWheel

CirculateRequest

FocusOut

Property

Colormap

Gravity

Reparent

Configure

KeyPress, Key

ResizeRequest

ConfigureRequest

KeyRelease

Unmap

Create

Leave

Visibility

Deactivate
"""

#It will alsoo always have an event modifier
"""
An event modifier(optional):

Control

Mod1, M1, Command

Alt

Mod2, M2, Option

Shift

Mod3, M3

Lock

Mod4, M4

Extended

Mod5, M5

Button1, B1

Meta, M

Button2, B2

Double

Button3, B3

Triple

Button4, B4

Quadruple

Button5, B5

"""

#The Event detail(optional)
"""
Every keymapping occurs and is captured by either the keysym mapping
e.g (B in <KeyPress-B>) or by using a key symbol abbreviated as keysym value off KP_Up

below is the manner in which the above patterns ought to be used!
widget.bind("<Button-1>").pack()


"""














































