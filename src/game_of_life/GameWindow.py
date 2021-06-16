import pyglet
from game_of_life.ModeState import ModeState
from game_of_life.SceneController import SceneController
from game_of_life.scenes.Menu import Menu
from game_of_life.scenes.Target import Target
from game_of_life.scenes.Free import Free

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        win_width, win_height = 860, 640
        super(GameWindow, self).__init__(win_width, win_height, *args, **kwargs)

        self.modes = {
            ModeState.MENU: SceneController(
                self.__switch_mode,
                {'menu': Menu},
                'menu'
            ),
            ModeState.FREE: SceneController(
                self.__switch_mode,
                {'free': Free},
                'free'
            ),
            ModeState.TARGET: SceneController(
                self.__switch_mode,
                {'target': Target},
                'target'
            )
        }
        self.__active_mode = self.modes[ModeState.MENU]

        __background_color = (80, 80, 80, 255)
        self.__background = pyglet.image.SolidColorImagePattern(__background_color).create_image(win_width, win_height)

        pyglet.clock.schedule_interval(self.update, .5)

    def __switch_mode(self, mode_state: ModeState):
        self.__active_mode = self.modes[mode_state]

    def on_mouse_press(self, x: int, y: int, button: int, _: int):
        self.__active_mode.active_scene.mouse_press(x, y, button)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        self.__active_mode.active_scene.mouse_release(x, y, button)

    def on_draw(self):
        self.__active_mode.active_scene.draw()
        #self.__background.blit(0, 0)

    def update(self, dt: float):
        print(self.__active_mode.active_scene.thing)