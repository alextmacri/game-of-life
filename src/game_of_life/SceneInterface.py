import pyglet
from typing import Callable
from game_of_life.ModeState import ModeState

class SceneInterface:
    """
    Represents a scene, in a mode in the game.

    switch_scene_cb: Callable[[str], None], the callable function from
    SceneController to switch scenes
    switch_mode_cb: Callable[[str], None], the callable function from GameWindow
    to switch modes
    main_batch: pyglet.graphics.Batch, the pyglet rendering batch that the
    scene's ui elements belongs to
    """

    def __init__(self, switch_scene_cb: Callable[[str], None],
                 switch_mode_cb: Callable[[ModeState], None]) -> None:
        """Initialize this Panel."""
        self.__switch_scene_cb
        self.__switch_mode_cb

        self.__main_batch
    
    def mouse_press(self, x: int, y: int) -> None:
        """Event handler for a mouse press"""
        pass

    def mouse_release(self, x: int, y: int) -> None:
        """Event handler for a mouse release"""
        pass

    def mouse_drag(self, x: int, y: int) -> None:
        """Event handler for a mouse drag"""
        pass

    def draw(self) -> None:
        """Draw the scene with the batch(es)"""
        pass