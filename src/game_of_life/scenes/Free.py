import pyglet
from game_of_life.SceneInterface import SceneInterface
from typing import Callable
from game_of_life.ModeState import ModeState
from game_of_life.ui.Button import Button
from game_of_life.CellState import CellState
from game_of_life.Cell import Cell

class Free(SceneInterface):
    def __init__(self, switch_scene_cb: Callable[[str], None], switch_mode_cb: Callable[[ModeState], None]) -> None:
        self.__switch_scene_cb = switch_scene_cb
        self.__switch_mode_cb = switch_mode_cb
        self.__is_active = False

        self.__main_batch = pyglet.graphics.Batch()
        self.__cell_group = pyglet.graphics.OrderedGroup(1)
        self.__backdrop_group = pyglet.graphics.OrderedGroup(2)
        self.__button_group = pyglet.graphics.OrderedGroup(3)
        self.__text_group = pyglet.graphics.OrderedGroup(4)

        self.__live_button = Button(
            650,
            500,
            'Live',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )
        self.__dead_button = Button(
            650,
            410,
            'Dead',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )

        self.__click_action = CellState.LIVE
        self.__live_button.set_is_pressed(True)

        self.__universe = []
        for y_cor in range(0, 640, 20):
            self.__universe.append([])
            for x_cor in range(0, 640, 20):
                self.__universe[-1].append(Cell(y_cor, x_cor, self.__main_batch, self.__cell_group))
        self.__live_cells = set()

        pyglet.clock.schedule_interval(self.__update_cells, .5)

    def set_is_active(self, is_active: bool) -> None:
        """"""
        pass
    
    def mouse_press(self, x: int, y: int) -> None:
        """Accounts for the event of a mouse press"""
        if self.__live_button.press_in_bounds(x, y):
            self.__live_button.set_is_pressed(True)
            self.__click_action = CellState.LIVE
            self.__dead_button.set_is_pressed(False)

        elif self.__dead_button.press_in_bounds(x, y):
            self.__dead_button.set_is_pressed(True)
            self.__click_action = CellState.DEAD
            self.__live_button.set_is_pressed(False)

        elif x <= 640:
            self.__click_cell(x, y)

    def mouse_release(self, x: int, y: int) -> None:
        """"""
        pass

    def mouse_drag(self, x: int, y: int) -> None:
        if 0 <= x <= 640 and 0 <= y <= 640:
            self.__click_cell(x, y)

    def draw(self) -> None:
        """Drawing the Scene"""
        self.__main_batch.draw()

    def __update_cells(self, dt: float) -> None:
        """Updating the scene after the previously specified interval"""
        if self.__is_active:
            pass

    def __click_cell(self, x: int, y: int) -> None:
        col = y//20
        row = x//20
        if self.__click_action == CellState.LIVE:
            self.__live_cells.add((col, row))
        else:
            if (col, row) in self.__live_cells:
                self.__live_cells.remove((col,row))
        self.__universe[col][row].switch_state(self.__click_action)
        print(self.__live_cells)