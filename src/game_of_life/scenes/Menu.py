import pyglet
from game_of_life.ModeState import ModeState
from game_of_life.SceneInterface import SceneInterface
from typing import Callable
from game_of_life.ModeState import ModeState
from game_of_life.ui.Button import Button

class Menu(SceneInterface):
    """
    Represents a menu scene, in a menu mode in the game.

    switch_scene_cb: Callable[[str], None], the callable function from
    SceneController to switch scenes
    switch_mode_cb: Callable[[str], None], the callable function from GameWindow
    to switch modes
    main_batch: pyglet.graphics.Batch, the pyglet rendering batch that the
    scene's ui element belongs to
    button_group: pyglet.graphics.OrderedGroup, the pyglet rendering group that the
    scene's button image sprites belong to
    text_group: pyglet.graphics.OrderedGroup, the pyglet rendering group that the
    scene's text belongs to
    title_text: pyglet.text.Label, the title text of the scene
    free_button: Button, the button to switch to free mode
    """

    def __init__(self, switch_scene_cb: Callable[[str], None],
                 switch_mode_cb: Callable[[ModeState], None]) -> None:
        """Initialize this Menu scene."""
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
        """Event handler for a mouse press."""
        # Sets the free button's is_pressed state to true if it's clicked
        if self.__free_button.press_in_bounds(x, y):
            self.__free_button.set_is_pressed(True)

    def mouse_release(self, x: int, y: int) -> None:
        """Event handler for a mouse release."""
        # Processes a free button click if it has been pressed, by switching to
        # free play mode
        if self.__free_button.get_is_pressed():
            self.__free_button.set_is_pressed(False)
            self.__switch_mode_cb(ModeState.FREE)

    def mouse_drag(self, x: int, y: int):
        """Event handler for a mouse drag."""
        # There isn't any mouse drag functionality in this scene, but this needs
        # to be here to prevent an error in GameWindow
        pass

    def draw(self) -> None:
        """Draw the scene with the batch."""
        self.__main_batch.draw()