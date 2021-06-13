import pyglet
from game_of_life.Cell import Cell

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(860, 640, *args, **kwargs)

        self.__mode_controller = None

        self.batch = pyglet.graphics.Batch()
        self.group = pyglet.graphics.OrderedGroup(1)
        self.cells = []
        for x_ in range(0, 640, 20):
            self.cells.append([])
            for y_ in range(0, 640, 20):
                self.cells[-1].append(Cell(x_, y_, self.batch, self.group))

        __background_color = (80, 80, 80, 255)
        self.__background = pyglet.image.SolidColorImagePattern(__background_color).create_image(860, 640)

        pyglet.clock.schedule_interval(self.update, .5)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        self.cells[y//20][x//20].switch_state(1)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)

    def on_draw(self):
        self.__background.blit(0, 0)
        self.batch.draw()

    def update(self, dt: float):
        print(dt)