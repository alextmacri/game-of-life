import pyglet
from game_of_life.ModeState import ModeState
from game_of_life.SceneController import SceneController
from game_of_life.scenes.Menu import Menu
from game_of_life.scenes.Target import Target
from game_of_life.scenes.Free import Free

class GameWindow(pyglet.window.Window):
    """
    Represents a pyglet window of the game.

    modes: dict[ModeState, SceneController], the dictionary of game modes
    active_mode: SceneController, the mode currently being displayed and updated
    background: the background sprite of the entire pyglet window
    """

    def __init__(self, *args, **kwargs):
        """Initialize this GameWindow."""
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

        # Setting up and creating the background sprite
        background_color = pyglet.image.SolidColorImagePattern(
            (80, 80, 80, 255)
        )
        background_image_data = background_color.create_image(
            win_width,
            win_height
        )
        self.__background = pyglet.sprite.Sprite(
            background_image_data,
            x=0,
            y=0
        )

    def __switch_mode(self, mode_state: ModeState) -> None:
        """
        Switch the current mode to the mode of mode_state by updating the active
        mode.
        """
        self.__active_mode = self.modes[mode_state]

    def on_mouse_press(self, x: int, y: int, *_) -> None:
        """
        Catch the mouse press event with the active mode's active scene's event
        handler for a mouse press.
        """
        self.__active_mode.active_scene.mouse_press(x, y)

    def on_mouse_release(self, x: int, y: int, *_) -> None:
        """
        Catch the mouse release event with the active mode's active scene's
        event handler for a mouse release.
        """
        self.__active_mode.active_scene.mouse_release(x, y)

    def on_mouse_drag(self, x: int, y: int, *_) -> None:
        """
        Catch the mouse drag event with the active mode's active scene's event
        handler for a mouse drag.
        """
        self.__active_mode.active_scene.mouse_drag(x, y)

    def on_draw(self) -> None:
        """
        Draw the background sprite and call the active mode's active scene's
        draw method.
        """
        self.__background.draw()
        self.__active_mode.active_scene.draw()