import pyglet
from typing import Callable

class SceneInterface:
    """"""

    def __init__(self, switch_scene_cb: Callable[[bool], None], switch_mode_cb: Callable[[bool], None]) -> None:
        self.__switch_scene_cb
        self.__switch_mode_cb
        self.__is_active

        self.__main_batch

    def set_is_active(self, is_active: bool) -> None:
        """"""
        pass
    
    def mouse_press(self, x: int, y: int, button: int) -> None:
        """Accounts for the event of a mouse press"""
        pass

    def mouse_release(self, x: int, y: int, button: int) -> None:
        """Accounts for the event of a mouse release"""
        pass

    def draw(self) -> None:
        """Drawing the Scene"""
        pass