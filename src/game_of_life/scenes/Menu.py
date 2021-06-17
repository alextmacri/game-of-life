import pyglet
from game_of_life.ModeState import ModeState
from game_of_life.SceneInterface import SceneInterface
from typing import Callable
from game_of_life.ModeState import ModeState
from game_of_life.ui.Button import Button

class Menu(SceneInterface):
    def __init__(self, switch_scene_cb: Callable[[str], None], switch_mode_cb: Callable[[ModeState], None]) -> None:
        self.__switch_scene_cb = switch_scene_cb
        self.__switch_mode_cb = switch_mode_cb
        self.__is_active = False

        self.thing = 'menu'

        self.__main_batch = pyglet.graphics.Batch()
        self.__cell_group = pyglet.graphics.OrderedGroup(1)
        self.__backdrop_group = pyglet.graphics.OrderedGroup(2)
        self.__button_group = pyglet.graphics.OrderedGroup(3)
        self.__text_group = pyglet.graphics.OrderedGroup(4)

        self.__free_button = Button(
            330,
            200,
            'Free Play',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )

    def set_is_active(self, is_active: bool) -> None:
        """"""
        self.__is_active = is_active
    
    def mouse_press(self, x: int, y: int) -> None:
        """Accounts for the event of a mouse press"""
        if self.__free_button.press_in_bounds(x, y):
            self.__free_button.set_is_pressed(True)

    def mouse_release(self, x: int, y: int) -> None:
        if self.__free_button.get_is_pressed():
            self.__free_button.set_is_pressed(False)
            self.__switch_mode_cb(ModeState.FREE)

    def mouse_drag(self, x: int, y: int):
        pass

    def draw(self) -> None:
        """Drawing the Scene"""
        self.__main_batch.draw()