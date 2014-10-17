##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=800,height=600, background='light blue')
drawpad.grid(row=0, column=1)
# 70pt: House outline (roof and the house)
square = drawpad.create_rectangle(200,200,250,250, fill='red')
line = drawpad.create_line(200,-250,250,200, fill= 'red')
line = drawpad.create_line(200,200,250,-200, fill= 'red')
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

root.mainloop()