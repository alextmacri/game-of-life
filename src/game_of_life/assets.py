import pyglet

# Setting up cell images
dead_rgba = (30, 30, 30, 255)
live_rgba = (225, 225, 225, 255)
cell_dead_image = pyglet.image.SolidColorImagePattern(dead_rgba).create_image(19, 19)
cell_live_image = pyglet.image.SolidColorImagePattern(live_rgba).create_image(19, 19)

# Setting up backdrop image generator
backdrop_rgba = (180, 100, 100, 180)
def backdrop_image_generator(width: int, height: int) -> pyglet.image.ImageData:
    return pyglet.image.SolidColorImagePattern(backdrop_rgba).create_image(width, height)

# Loading button images
button_pressed_image = pyglet.image.load('src/assets/button_pressed.png')
button_unpressed_image = pyglet.image.load('src/assets/button_unpressed.png')

# Loading custom font
pyglet.font.add_file('src/assets/BACK_TO_1982.ttf')
back_to_1982 = pyglet.font.load('Back to 1982')