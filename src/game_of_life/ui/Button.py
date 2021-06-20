import pyglet
from game_of_life.assets import button_pressed_image, button_unpressed_image

class Button:
    """
    Represents a button in the pyglet window of the game.

    is_pressed: bool, the state of the button being pressed or not
    x_cor: int, the x coordinates of the left of the button when drawn in the
    game window
    y_cor: int, the y coordinates of the bottom of the button when drawn in the
    game window
    x_cor_end: int, the x coordinates of the right of the button when drawn in
    the game window
    y_cor_end: int, the y coordinates of the top of the button when drawn in the
    game window
    batch: pyglet.graphics.Batch, the pyglet rendering batch that the button's
    ui element belongs to
    button_group: pyglet.graphics.OrderedGroup, the pyglet rendering group that the
    button's button image sprite belongs to
    text_group: pyglet.graphics.OrderedGroup, the pyglet rendering group that the
    button's text belongs to
    label: pyglet.text.Label, the text on the button
    images: dict[bool, pyglet.image.ImageData], the images that a button uses in
    each state of being pressed
    sprite: pyglet.sprite.Sprite, the current sprite of the button
    """

    def __init__(self, x_cor: int, y_cor: int, text: str,
                 batch: pyglet.graphics.Batch,
                 button_group: pyglet.graphics.OrderedGroup,
                 text_group: pyglet.graphics.OrderedGroup) -> None:
        """Initialize this Button."""
        self.__is_pressed = False

        width = 200
        height = 80
        self.__x_cor = x_cor
        self.__y_cor = y_cor
        self.__x_cor_end = x_cor + width
        self.__y_cor_end = y_cor + height

        self.__batch = batch
        self.__button_group = button_group
        self.__text_group = text_group

        label_x = width//2 + self.__x_cor
        label_y = height//2 + self.__y_cor
        self.__label = pyglet.text.Label(
            text,
            font_name='Back to 1982',
            font_size=12,
            color=(0, 0, 0, 255),
            x=label_x,
            y=label_y,
            anchor_x='center',
            anchor_y='center',
            batch=self.__batch,
            group=self.__text_group
        )

        self.__images = {
            True: button_pressed_image,
            False: button_unpressed_image
        }

        self.__sprite = self.__define_sprite()

    def get_is_pressed(self) -> bool:
        """Return the value of is_pressed."""
        return self.__is_pressed

    def set_is_pressed(self, is_pressed: bool) -> None:
        """
        Set the value of is_pressed (attribute) to is_pressed (argument), and
        update the sprite by deleting the current sprite, and making a new one
        in its place.
        """
        self.__is_pressed = is_pressed
        self.__sprite.delete()
        self.__sprite = self.__define_sprite()

    def press_in_bounds(self, x: int, y: int) -> bool:
        """Return if the x and y are in the bounds of the button."""
        x_in_bounds = self.__x_cor <= x <= self.__x_cor_end
        y_in_bounds = self.__y_cor <= y <= self.__y_cor_end
        return x_in_bounds and y_in_bounds

    def __define_sprite(self) -> pyglet.sprite.Sprite:
        """Define the button, using the other class attributes."""
        # Uses button_pressed_image if the button is pressed, and
        # button_unpressed_image if the button is unpressed
        return pyglet.sprite.Sprite(
            self.__images[self.__is_pressed],
            x=self.__x_cor,
            y=self.__y_cor,
            batch=self.__batch,
            group=self.__button_group
        )