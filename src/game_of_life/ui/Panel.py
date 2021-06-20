import pyglet
from game_of_life.assets import backdrop_image_generator
from game_of_life.ui.Button import Button

class Panel:
    """"""

    def __init__(self, x_cor: int, y_cor: int, text: str, panel_batch: pyglet.graphics.Batch, backdrop_group: pyglet.graphics.OrderedGroup, button_group: pyglet.graphics.OrderedGroup, text_group: pyglet.graphics.OrderedGroup) -> None:
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
        return self.__is_showing

    def set_is_showing(self, is_showing: bool) -> None:
        self.__is_showing = is_showing