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
square = drawpad.create_rectangle(200,200,550,550, fill='red')
line = drawpad.create_line(375,150,550,200)
line = drawpad.create_line(200,200,375,150)
# 80pt: Square windows and a door
window = drawpad.create_rectangle(245,245,310,320, fill='light yellow')
window2 = drawpad. create_rectangle(445,245,510,320, fill= 'light yellow')
door = drawpad. create_rectangle(325,425,425,550, fill='light green')
# 90pt: A door handle plus a chimney!
doorHandle = drawpad. create_oval(335,495,345,485, fill='brown')

# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

root.mainloop()