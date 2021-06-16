import pyglet
from game_of_life.ModeState import ModeState
from game_of_life.SceneInterface import SceneInterface
from typing import Callable

class Menu(SceneInterface):
    def __init__(self, switch_scene_cb: Callable[[bool], None], switch_mode_cb: Callable[[bool], None]) -> None:
        self.__switch_scene_cb = switch_scene_cb
        self.__switch_mode_cb = switch_mode_cb
        self.__is_active = False

        self.__main_batch = pyglet.graphics.Batch()
        self.__cell_group = pyglet.graphics.OrderedGroup(1)
        self.__backdrop_group = pyglet.graphics.OrderedGroup(2)
        self.__ui_group = pyglet.graphics.OrderedGroup(3)
        self.thing = 'menu'

    def set_is_active(self, is_active: bool) -> None:
        """"""
        self.__is_active = is_active
    
    def mouse_press(self, x: int, y: int, button: int) -> None:
        """Accounts for the event of a mouse press"""
        print(self.__is_active)
        print('switched')
        self.__switch_mode_cb(ModeState.FREE)

    def mouse_release(self, x: int, y: int, button: int) -> None:
        """Accounts for the event of a mouse release"""
        pass

    def draw(self) -> None:
        """Drawing the Scene"""
        self.__main_batch.draw()