import pyglet
from game_of_life.SceneInterface import SceneInterface
from typing import Callable
from game_of_life.ModeState import ModeState
from game_of_life.Cell import Cell
from game_of_life.CellState import CellState

class Free(SceneInterface):
    def __init__(self, switch_scene_cb: Callable[[str], None], switch_mode_cb: Callable[[ModeState], None]) -> None:
        self.__switch_scene_cb = switch_scene_cb
        self.__switch_mode_cb = switch_mode_cb
        self.__is_active = False

        self.__main_batch = pyglet.graphics.Batch()
        self.__cell_group = pyglet.graphics.OrderedGroup(1)
        self.__backdrop_group = pyglet.graphics.OrderedGroup(2)
        self.__ui_group = pyglet.graphics.OrderedGroup(3)

        self.__click_action = CellState.LIVE

        self.__universe = []
        for y_cor in range(0, 640, 20):
            self.__universe.append([])
            for x_cor in range(0, 640, 20):
                self.__universe[-1].append(Cell(y_cor, x_cor, self.__main_batch, self.__cell_group))

    def set_is_active(self, is_active: bool) -> None:
        """"""
        pass
    
    def mouse_press(self, x: int, y: int) -> None:
        """Accounts for the event of a mouse press"""
        if x <= 640:
            self.__universe[y//20][x//20].switch_state(self.__click_action)
            print(self.__universe)

    def mouse_release(self, x: int, y: int) -> None:
        """"""
        pass

    def mouse_drag(self, x: int, y: int):
        if 0 <= x <= 640 and 0 <= y <= 640:
            self.__universe[y//20][x//20].switch_state(self.__click_action)

    def draw(self) -> None:
        """Drawing the Scene"""
        self.__main_batch.draw()

    def update_cells(self, dt: float) -> None:
        """Updating the scene after the previously specified interval"""
        if self.__is_active:
            pass