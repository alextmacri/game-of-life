"""
Sample GUI using the tkinter library and its canvas system.

Includes shapes, images, labels, buttons, and keypresses.
"""

from tkinter import *

# Initialize the root window with a title and dimensions
root = Tk()
root.title('Sample Program')
root.geometry('600x600')

# Initialize the canvas (everything gets drawn on here)
canvas = Canvas(root, height=600, width=600)
canvas.pack()

# Functions

def clear_canvas() -> None:
    """Clear the parts of the canvas that need to be cleared."""
    for key in ['background', 'moon', 'sun']:
        if key in shapes and shapes[key] is not None:
            canvas.delete(shapes[key])
            shapes[key] = None

def draw_night() -> None:
    """Draw the night scene."""
    global earth, earth_x, earth_y
    clear_canvas()

    background = canvas.create_rectangle(0, 0, 800, 800, fill='black')
    shapes['background'] = background

    moon = canvas.create_oval(425, 350, 475, 400, fill='white')
    shapes['moon'] = moon

    # Move earth above the background too
    canvas.tag_raise(earth)

    # Stars?

def draw_day() -> None:
    """Draw the day scene."""
    clear_canvas()

    background = canvas.create_rectangle(0, 0, 800, 800, fill='#b1e8f2')
    shapes['background'] = background

    sun = canvas.create_oval(50, 200, 250, 400, fill='yellow')
    shapes['sun'] = sun

    # Move earth above the background too
    canvas.tag_raise(earth)

    # Cloud?

def add_day() -> None:
    """Add a day to the counter and schedule the next one."""
    global n_days
    n_days += 1
    days_text.set(f'Days: {n_days}')
    root.after(3000, add_day)

def toggle_day_night() -> None:
    """Toggle whether to draw day or night."""
    global is_night
    is_night = not is_night
    if is_night:
        draw_night()
    else:
        draw_day()

def move(event) -> None:
    """Move the earth object using WASD."""
    print(canvas.coords(earth))
    
    if event.char == 'w':
        if canvas.coords(earth)[1] > 0:
            canvas.move(earth, 0, -20)
    elif event.char == 's':
        if canvas.coords(earth)[1] < 480:
            canvas.move(earth, 0, 20)
    elif event.char == 'a':
        if canvas.coords(earth)[0] > 0:
            canvas.move(earth, -20, 0)
    elif event.char == 'd':
        if canvas.coords(earth)[0] < 480:
            canvas.move(earth, 20, 0)

# Add a label to track the days
days_text = StringVar() # Allows us to update it later
days_text.set('Days: 0')
days_label = Label(canvas, textvariable=days_text, fg='white', bg='black', font=("Courier", 16))
days_label.pack()
canvas.create_window(300, 20, window=days_label)

# Add a label with instructions
instructions_text = """A day passes every 3 seconds.
Press up, down, left, right to move the earth.
Click the button to toggle day/night."""
instructions_label = Label(canvas, text=instructions_text, fg='white', bg='black', font=("Courier", 11))
instructions_label.pack()
canvas.create_window(300, 80, window=instructions_label)

# Add a button to toggle day/night
toggle_button = Button(root, text = "Day/night", command=toggle_day_night)
canvas.create_window(300, 150, window=toggle_button)

# Global resources
global n_days, is_night
n_days = 0
is_night = False
shapes = {}
earth_image = PhotoImage(file='src/assets/earth.png')
earth = canvas.create_image(300, 400, anchor=NW, image=earth_image)
shapes['earth'] = earth

# Bind keypresses
root.bind("<Key>", move)

# Draw the initial scene
draw_day()
    
# Schedule the day counter
root.after(3000, add_day)

# This always has to be the very last thing
root.mainloop()
