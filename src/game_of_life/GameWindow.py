import pyglet

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(800, 600, *args, **kwargs)

        __background_color = (50, 50, 50, 255)
        self.__background = pyglet.image.SolidColorImagePattern(__background_color).create_image(800, 600)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)

    def on_draw(self):
        self.__background.blit(0, 0)

    def update(self, dt: float):
        pass