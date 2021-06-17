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

        self.__main_batch = pyglet.graphics.Batch()
        self.__cell_group = pyglet.graphics.OrderedGroup(1)
        self.__backdrop_group = pyglet.graphics.OrderedGroup(2)
        self.__button_group = pyglet.graphics.OrderedGroup(3)
        self.__text_group = pyglet.graphics.OrderedGroup(4)

        self.__play_button = Button(
            650,
            500,
            'Play',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )
        self.__stop_button = Button(
            650,
            410,
            'Stop',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )
        self.__stop_button.set_is_pressed(True)
        self.__is_active = False

        self.__live_button = Button(
            650,
            270,
            'Live',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )
        self.__dead_button = Button(
            650,
            180,
            'Dead',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )
        self.__live_button.set_is_pressed(True)
        self.__click_action = CellState.LIVE

        self.__reset_button = Button(
            650,
            40,
            'Reset',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )

        self.__universe = self.__generate_universe()
        self.__prev_universe_states = self.__generate_universe_states()
        self.__live_cells = set()

        pyglet.clock.schedule_interval(self.__update_cells, .4)

    def set_is_active(self, is_active: bool) -> None:
        """"""
        pass
    
    def mouse_press(self, x: int, y: int) -> None:
        """Accounts for the event of a mouse press"""
        if self.__play_button.press_in_bounds(x, y):
            self.__play_button.set_is_pressed(True)
            self.__is_active = True
            self.__stop_button.set_is_pressed(False)
        elif self.__stop_button.press_in_bounds(x, y):
            self.__stop_button.set_is_pressed(True)
            self.__is_active = False
            self.__play_button.set_is_pressed(False)
        
        if not self.__is_active:
            if self.__live_button.press_in_bounds(x, y):
                self.__live_button.set_is_pressed(True)
                self.__click_action = CellState.LIVE
                self.__dead_button.set_is_pressed(False)
            elif self.__dead_button.press_in_bounds(x, y):
                self.__dead_button.set_is_pressed(True)
                self.__click_action = CellState.DEAD
                self.__live_button.set_is_pressed(False)

            elif self.__reset_button.press_in_bounds(x, y):
                self.__reset_button.set_is_pressed(True)

            elif x <= 639:
                self.__click_cell(x, y)

    def mouse_release(self, x: int, y: int) -> None:
        """"""
        if self.__reset_button.get_is_pressed():
            self.__reset_button.set_is_pressed(False)
            self.__universe = self.__generate_universe()
            self.__live_cells = set()


    def mouse_drag(self, x: int, y: int) -> None:
        if not self.__is_active:
            if 0 <= x <= 639 and 0 <= y <= 639:
                self.__click_cell(x, y)

    def draw(self) -> None:
        """Drawing the Scene"""
        self.__main_batch.draw()

    def __update_cells(self, dt: float) -> None:
        """Updating the scene after the previously specified interval"""
        def in_bounds(coordinates: tuple[int]):
            x = 0 <= coordinates[0] < 32
            y = 0 <= coordinates[1] < 32
            return x and y

        if self.__is_active:
            make_dead = []
            live_surrounding_dead = {}

            offsets = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

            for cell in self.__live_cells:
                dead_surrounding_live = 0

                for offset in offsets:
                    coord = (cell[0] + offset[0], cell[1] + offset[1])

                    if in_bounds(coord):
                        if self.__universe[coord[0]][coord[1]].state == CellState.DEAD:
                            dead_surrounding_live += 1

                            if coord in live_surrounding_dead:
                                live_surrounding_dead[coord] += 1
                            else:
                                live_surrounding_dead[coord] = 1
                    else:
                        dead_surrounding_live += 1

                if 8 - dead_surrounding_live not in [2, 3]:
                    make_dead.append(cell)

            for coord in make_dead:
                if coord in self.__live_cells:
                    self.__live_cells.remove(coord)
                    self.__universe[coord[0]][coord[1]].switch_state(CellState.DEAD)

            for coord, counter in live_surrounding_dead.items():
                if counter == 3 and in_bounds(coord):
                    self.__universe[coord[0]][coord[1]].switch_state(CellState.LIVE)
                    self.__live_cells.add(coord)
        
            if self.__prev_universe_states == self.__universe:
                self.__stop_button.set_is_pressed(True)
                self.__is_active = False
                self.__play_button.set_is_pressed(False)
            else:
                self.__prev_universe_states = self.__generate_universe_states()

    def __click_cell(self, x: int, y: int) -> None:
        col = y//20
        row = x//20
        if self.__click_action == CellState.LIVE:
            self.__live_cells.add((col, row))
        else:
            if (col, row) in self.__live_cells:
                self.__live_cells.remove((col,row))
        self.__universe[col][row].switch_state(self.__click_action)
    
    def __generate_universe(self) -> list[tuple[Cell]]:
        """"""
        universe = []
        for y_cor in range(0, 640, 20):
            universe.append([])
            for x_cor in range(0, 640, 20):
                universe[-1].append(Cell(y_cor, x_cor, self.__main_batch, self.__cell_group))
        return universe

    def __generate_universe_states(self) -> list[tuple[CellState]]:
        return [[cell.state for cell in row] for row in self.__universe]