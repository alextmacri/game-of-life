import pyglet
from game_of_life.assets import button_pressed_image, button_unpressed_image

class Button:
    """"""

    def __init__(self, x_cor: int, y_cor: int, text: str, batch: pyglet.graphics.Batch, button_group: pyglet.graphics.OrderedGroup, text_group: pyglet.graphics.OrderedGroup) -> None:
        self.is_active = True
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

        self.__click_sound = None

        self.__images = {
            True: button_pressed_image,
            False: button_unpressed_image
        }

        self.__sprite = self.__define_sprite()

    def get_is_pressed(self) -> bool:
        return self.__is_pressed

    def set_is_pressed(self, is_pressed: bool) -> None:
        self.__is_pressed = is_pressed
        self.__sprite.delete()
        self.__sprite = self.__define_sprite()

    def press_in_bounds(self, x: int, y: int) -> bool:
        x_in_bounds = self.__x_cor <= x <= self.__x_cor_end
        y_in_bounds = self.__y_cor <= y <= self.__y_cor_end
        return x_in_bounds and y_in_bounds

    def __define_sprite(self) -> pyglet.sprite.Sprite:
        return pyglet.sprite.Sprite(
            self.__images[self.__is_pressed],
            x=self.__x_cor,
            y=self.__y_cor,
            batch=self.__batch,
            group=self.__button_group
        )