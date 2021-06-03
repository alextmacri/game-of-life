from tkinter import *

# Create a root
root = Tk()
root.title('My very first GUI')
root.geometry('400x400')

# Create a canvas
canvas = Canvas(root, height=400, width=400)
canvas.pack()

# Create a background
background = canvas.create_rectangle(0, 0, 200, 200, fill='black')

# Make the root go
root.mainloop()
