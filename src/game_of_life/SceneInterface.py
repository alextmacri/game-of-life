import pyglet
from typing import Callable
from game_of_life.ModeState import ModeState

class SceneInterface:
    """"""

    def __init__(self, switch_scene_cb: Callable[[str], None], switch_mode_cb: Callable[[ModeState], None]) -> None:
        self.__switch_scene_cb
        self.__switch_mode_cb
        self.__is_active

        self.__main_batch

    def set_is_active(self, is_active: bool) -> None:
        """"""
        pass
    
    def mouse_press(self, x: int, y: int) -> None:
        """Accounts for the event of a mouse press"""
        pass

    def mouse_drag(self, x: int, y: int):
        """"""
        pass

    def draw(self) -> None:
        """Drawing the Scene"""
        pass