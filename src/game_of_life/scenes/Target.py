import pyglet
from game_of_life.SceneInterface import SceneInterface
from typing import Callable
from game_of_life.ModeState import ModeState

class Target(SceneInterface):
    def __init__(self, switch_scene_cb: Callable[[str], None], switch_mode_cb: Callable[[ModeState], None]) -> None:
        self.__switch_scene_cb = switch_scene_cb
        self.__switch_mode_cb = switch_mode_cb
        self.__is_active = False

        self.__main_batch = pyglet.graphics.Batch()
        self.__cell_group = pyglet.graphics.OrderedGroup(1)
        self.__backdrop_group = pyglet.graphics.OrderedGroup(2)
        self.__ui_group = pyglet.graphics.OrderedGroup(3)

    def set_is_active(self, is_active: bool) -> None:
        """"""
        pass
    
    def mouse_press(self, x: int, y: int) -> None:
        """Accounts for the event of a mouse press"""
        pass

    def mouse_release(self, x: int, y: int) -> None:
        """"""
        pass

    def mouse_drag(self, x: int, y: int):
        pass

    def draw(self) -> None:
        """Drawing the Scene"""
        self.__main_batch.draw()

    def update(self, dt: float) -> None:
        """Updating the scene after the previously specified interval"""
        pass