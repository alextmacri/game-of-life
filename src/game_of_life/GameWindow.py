import pyglet
from game_of_life.Cell import Cell
from game_of_life.ModeController import ModeController
from game_of_life.ModeState import ModeState
from game_of_life.Mode import Mode
from game_of_life.SceneController import SceneController
from game_of_life.scenes.Menu import Menu
from game_of_life.scenes.Target import Target
from game_of_life.scenes.Free import Free

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(GameWindow, self).__init__(860, 640, *args, **kwargs)

        self.__mode_controller = ModeController(
            {
                ModeState.MENU: Mode(
                    SceneController(
                        {'menu': Menu()},
                        'menu'
                    )
                ),
                ModeState.FREE: Mode(
                    SceneController(
                        {'free': Free()},
                        'free'
                    )
                ),
                ModeState.TARGET: Mode(
                    SceneController(
                        {'target': Target()},
                        'target'
                    )
                )
            },
            ModeState.MENU
        )

        for mode_key in self.__mode_controller.modes:
            mode = self.__mode_controller.modes[mode_key]
            for scene_key in mode.scene_controller.scenes:
                mode.scene_controller.scenes[scene_key].parent_mode_controller = self.__mode_controller
                mode.scene_controller.scenes[scene_key].parent_scene_controller = mode.scene_controller

        # self.batch = pyglet.graphics.Batch()
        # self.group = pyglet.graphics.OrderedGroup(1)
        # self.cells = []
        # for x_ in range(0, 640, 20):
        #     self.cells.append([])
        #     for y_ in range(0, 640, 20):
        #         self.cells[-1].append(Cell(x_, y_, self.batch, self.group))

        __background_color = (80, 80, 80, 255)
        self.__background = pyglet.image.SolidColorImagePattern(__background_color).create_image(860, 640)

        pyglet.clock.schedule_interval(self.update, .5)

    def on_mouse_press(self, x: int, y: int, button: int, _: int):
        # self.cells[y//20][x//20].switch_state(1)
        self.__mode_controller.active_mode.scene_controller.active_scene.mouse_press(x, y, button)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        print(x, y)

    def on_draw(self):
        self.__background.blit(0, 0)
        # self.batch.draw()

    def update(self, dt: float):
        print(self.__mode_controller.active_mode.scene_controller.active_scene.thing)