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
        __background_image_data = pyglet.image.SolidColorImagePattern(__background_color).create_image(win_width, win_height)
        self.__background = pyglet.sprite.Sprite(__background_image_data, x=0, y=0)

        pyglet.clock.schedule_interval(self.update, .5)

    def __switch_mode(self, mode_state: ModeState):
        self.__active_mode = self.modes[mode_state]

    def on_mouse_press(self, x: int, y: int, *_):
        self.__active_mode.active_scene.mouse_press(x, y)

    def on_mouse_release(self, x: int, y: int, *_):
        self.__active_mode.active_scene.mouse_release(x, y)

    def on_mouse_drag(self, x: int, y: int, *_):
        self.__active_mode.active_scene.mouse_drag(x, y)

    def on_draw(self):
        self.__background.draw()
        self.__active_mode.active_scene.draw()

    def update(self, dt: float):
        print(self.__active_mode.active_scene.thing)