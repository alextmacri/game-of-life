import pyglet

# Loading the images as variables of the pyglet.image.ImageData type
dead_rgba = (30, 30, 30, 255)
live_rgba = (225, 225, 225, 255)
cell_dead_image = pyglet.image.SolidColorImagePattern(dead_rgba).create_image(19, 19)
cell_live_image = pyglet.image.SolidColorImagePattern(live_rgba).create_image(19, 19)