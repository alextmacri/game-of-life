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

        self.__main_batch = pyglet.graphics.Batch()
        self.__button_group = pyglet.graphics.OrderedGroup(1)
        self.__text_group = pyglet.graphics.OrderedGroup(2)

        self.__title_text = pyglet.text.Label(
            "The Game of Life: The Game",
            font_name='Back to 1982',
            font_size=28,
            color=(0, 0, 0, 255),
            x=430,
            y=480,
            anchor_x='center',
            anchor_y='center',
            batch=self.__main_batch,
            group=self.__text_group
        )

        self.__free_button = Button(
            330,
            200,
            'Free Play',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )
    
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