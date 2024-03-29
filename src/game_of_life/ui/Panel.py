import pyglet
from game_of_life.assets import backdrop_image_generator
from game_of_life.ui.Button import Button

class Panel:
    """
    Represents a button in the pyglet window of the game.

    is_showing: bool, the state of the panel being updated and rendered or not
    x_cor: int, the x coordinates of the left of the button when drawn in the
    game window
    y_cor: int, the y coordinates of the bottom of the button when drawn in the
    game window
    batch: pyglet.graphics.Batch, the pyglet rendering batch that the panel's
    ui element belongs to
    backdrop_group: pyglet.graphics.OrderedGroup, the pyglet rendering group that the
    panel's backdrop image sprite belongs to
    button_group: pyglet.graphics.OrderedGroup, the pyglet rendering group that the
    panel's button image sprites belong to
    text_group: pyglet.graphics.OrderedGroup, the pyglet rendering group that the
    panel's text belongs to
    label: pyglet.text.Label, the title text of the panel
    continue_button: Button, the button to close the pause panel and unpause
    exit_button: Button, the button to return you to the main menu
    """

    def __init__(self, x_cor: int, y_cor: int, text: str, panel_batch: pyglet.graphics.Batch, backdrop_group: pyglet.graphics.OrderedGroup, button_group: pyglet.graphics.OrderedGroup, text_group: pyglet.graphics.OrderedGroup) -> None:
        """Initialize this Panel."""
        self.__is_showing = False

        width = 220
        height = 300
        self.__x_cor = x_cor
        self.__y_cor = y_cor

        self.__panel_batch = panel_batch
        self.__backdrop_group = backdrop_group
        self.__button_group = button_group
        self.__text_group = text_group

        self.__backdrop = pyglet.sprite.Sprite(
            backdrop_image_generator(width, height),
            x=self.__x_cor,
            y=self.__y_cor,
            batch=self.__panel_batch,
            group=self.__backdrop_group
        )

        label_x = width//2 + self.__x_cor
        label_y = self.__y_cor + height - height // 4
        self.__label = pyglet.text.Label(
            text,
            font_name='Back to 1982',
            font_size=22,
            color=(0, 0, 0, 255),
            x=label_x,
            y=label_y,
            anchor_x='center',
            anchor_y='center',
            batch=self.__panel_batch,
            group=self.__text_group
        )

        self.continue_button = Button(
            self.__x_cor + 10,
            self.__y_cor + 100,
            'Continue',
            self.__panel_batch,
            self.__button_group,
            self.__text_group
        )
        self.exit_button = Button(
            self.__x_cor + 10,
            self.__y_cor + 10,
            'Exit',
            self.__panel_batch,
            self.__button_group,
            self.__text_group
        )

    def get_is_showing(self) -> bool:
        """Return the value of is_pressed."""
        return self.__is_showing

    def set_is_showing(self, is_showing: bool) -> None:
        """Set the value of is_showing (attribute) to is_showing (argument)."""
        self.__is_showing = is_showing