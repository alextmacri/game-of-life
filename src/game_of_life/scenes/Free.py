import pyglet
from game_of_life.SceneInterface import SceneInterface
from typing import Callable
from game_of_life.ModeState import ModeState
from game_of_life.ui.Button import Button
from game_of_life.ui.Panel import Panel
from game_of_life.CellState import CellState
from game_of_life.Cell import Cell

class Free(SceneInterface):
    """
    Represents a free play scene, in a free play mode in the game.

    switch_scene_cb: Callable[[str], None], the callable function from
    SceneController to switch scenes
    switch_mode_cb: Callable[[str], None], the callable function from GameWindow
    to switch modes
    main_batch: pyglet.graphics.Batch, the pyglet rendering batch that the
    scene's ui elements belong to
    panel_batch: pyglet.graphics.Batch, the pyglet rendering batch that the
    scene's panel and its ui elements belong to
    cell_group: pyglet.graphics.OrderedGroup, the pyglet rendering group that
    the scene's cell sprites belong to
    backdrop_group: pyglet.graphics.OrderedGroup, the pyglet rendering group
    that the scene's backdrop image sprites belong to
    button_group: pyglet.graphics.OrderedGroup, the pyglet rendering group that
    the scene's button image sprites belong to
    text_group: pyglet.graphics.OrderedGroup, the pyglet rendering group that the
    scene's text belongs to
    pause_button: Button, the button to pause the game and open the pause panel
    forward_button: Button, the button to update the universe a single time
    play_button: Button, the button to set is_active to True
    stop_button: Button, the button to set is_active to False
    is_active: bool, the state of if the game is updating or not
    live_button: Button, the button to set the click_action to CellState.LIVE
    dead_button: Button, the button to set the click_action to CellState.DEAD
    click_action: CellState, the state of what the clicked on cell's will be
    changed to
    reset_button: Button, the button to reset the universe to its default state
    pause_panel: Panel, the panel for the pause menu
    universe: list[list[Cell]], the universe of cells; where the Game of Life
    takes place
    prev_universe_states: list[list[CellState]], the array of cell states of the
    previous update of the universe
    live_cells: set[tuple[int]], the set of all the live cells' universe array
    (not screen) coordinates, in a tuple
    """

    def __init__(self, switch_scene_cb: Callable[[str], None],
                 switch_mode_cb: Callable[[ModeState], None]) -> None:
        """Initialize this Menu scene."""
        self.__switch_scene_cb = switch_scene_cb
        self.__switch_mode_cb = switch_mode_cb

        # Instantiating the large amount of batches and groups
        self.__main_batch = pyglet.graphics.Batch()
        self.__panel_batch = pyglet.graphics.Batch()
        self.__cell_group = pyglet.graphics.OrderedGroup(1)
        self.__backdrop_group = pyglet.graphics.OrderedGroup(2)
        self.__button_group = pyglet.graphics.OrderedGroup(3)
        self.__text_group = pyglet.graphics.OrderedGroup(4)

        # Instantiating the buttons. The y value decreases by 90 each time to
        # give 10px of inbetween space between buttons
        self.__pause_button = Button(
            650,
            550,
            'Pause Game',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )
        
        self.__forward_button = Button(
            650,
            460,
            'Forward',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )

        self.__play_button = Button(
            650,
            370,
            'Play',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )
        self.__stop_button = Button(
            650,
            280,
            'Stop',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )
        self.__stop_button.set_is_pressed(True) # The game starts off stopped
        self.__is_active = False

        self.__live_button = Button(
            650,
            190,
            'Live',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )
        self.__dead_button = Button(
            650,
            100,
            'Dead',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )
        self.__live_button.set_is_pressed(True) # You start by making them live
        self.__click_action = CellState.LIVE

        self.__reset_button = Button(
            650,
            10,
            'Reset',
            self.__main_batch,
            self.__button_group,
            self.__text_group
        )

        self.__pause_panel = Panel(
            210,
            170,
            'Paused',
            self.__panel_batch,
            self.__backdrop_group,
            self.__button_group,
            self.__text_group
        )

        self.__universe = self.__generate_universe()
        self.__prev_universe_states = self.__generate_universe_states()
        self.__live_cells = set()

        # Scheduling the update universe call
        pyglet.clock.schedule_interval(self.__update_universe, .3)
    
    def mouse_press(self, x: int, y: int) -> None:
        """Event handler for a mouse press."""
        
        # Checking the pause panel buttons if the pause panel is open
        if self.__pause_panel.get_is_showing():
            if self.__pause_panel.continue_button.press_in_bounds(x, y):
                self.__pause_panel.set_is_showing(False)
            elif self.__pause_panel.exit_button.press_in_bounds(x, y):
                self.__reset_scene()
                self.__switch_mode_cb(ModeState.MENU)
        # Checking the sidebar buttons and universe if the pause panel isn't
        # open
        else:
            # Checking the start and stop buttons
            if self.__pause_button.press_in_bounds(x, y):
                self.__pause_button.set_is_pressed(True)
            elif self.__play_button.press_in_bounds(x, y):
                self.__play_button.set_is_pressed(True)
                self.__is_active = True
                self.__stop_button.set_is_pressed(False)
            elif self.__stop_button.press_in_bounds(x, y):
                self.__stop_button.set_is_pressed(True)
                self.__is_active = False
                self.__play_button.set_is_pressed(False)
            # Checking the rest of the sidebar buttons and the universe if the
            # game isn't updating
            if not self.__is_active:
                if self.__forward_button.press_in_bounds(x, y):
                    self.__forward_button.set_is_pressed(True)

                elif self.__live_button.press_in_bounds(x, y):
                    self.__live_button.set_is_pressed(True)
                    self.__click_action = CellState.LIVE
                    self.__dead_button.set_is_pressed(False)
                elif self.__dead_button.press_in_bounds(x, y):
                    self.__dead_button.set_is_pressed(True)
                    self.__click_action = CellState.DEAD
                    self.__live_button.set_is_pressed(False)

                elif self.__reset_button.press_in_bounds(x, y):
                    self.__reset_button.set_is_pressed(True)

                # Checking the universe if it's in bounds for the click
                elif x <= 639:
                    self.__click_cell(x, y)

    def mouse_release(self, x: int, y: int) -> None:
        """Event handler for a mouse release."""
        # Unpresses button and processes button action/intention (pauses)
        if self.__pause_button.get_is_pressed():
            self.__pause_button.set_is_pressed(False)
            self.__pause_panel.set_is_showing(True)

        # Processes button action/intention (pauses) and unpresses the button
        elif self.__forward_button.get_is_pressed():
            # The action is processed first so it passes a check, and the 0 is
            # the delta time, since that's also a function that's scheduled
            self.__update_universe(0)
            self.__forward_button.set_is_pressed(False)

        # Unpresses button and processes button action/intention (resets)
        elif self.__reset_button.get_is_pressed():
            self.__reset_button.set_is_pressed(False)
            self.__universe = self.__generate_universe()
            self.__live_cells = set()

    def mouse_drag(self, x: int, y: int) -> None:
        """Event handler for a mouse drag."""
        # Checking the universe if the universe isn't updating, the game isn't
        # paused, and it's in bounds for the click
        if not self.__is_active and not self.__pause_panel.get_is_showing():
            if 0 <= x <= 639 and 0 <= y <= 639:
                self.__click_cell(x, y)

    def draw(self) -> None:
        """Draw the scene with the batches."""
        self.__main_batch.draw()
        if self.__pause_panel.get_is_showing():
            self.__panel_batch.draw()

    def __update_universe(self, _: int) -> None:
        """Update the universe with the classic Game of Life rules."""
        # Function to check if a cell won't cause an IndexError, or loop back to
        # the beginning
        def in_bounds(coordinates: tuple[int]):
            x = 0 <= coordinates[0] < 32
            y = 0 <= coordinates[1] < 32
            return x and y

        if not self.__pause_panel.get_is_showing(): # If the game isn't paused...
            # Runs the next block if the forward button has been pressed, or the
            # game is updating
            if self.__forward_button.get_is_pressed() or self.__is_active:
                # Makes list and dict for these so they can be run through at
                # the end, so it adheres to the Game of Life updating rules
                make_dead = []
                live_surrounding_dead = {}

                # The offsets for the 8 surrounding cells
                offsets = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

                for cell in self.__live_cells:
                    dead_surrounding_live = 0

                    # Looping through the 8 surrounding cells
                    for offset in offsets:
                        coord = (cell[0] + offset[0], cell[1] + offset[1])

                        if in_bounds(coord):
                            if self.__universe[coord[0]][coord[1]].state == CellState.DEAD:
                                # Adds to counter for original live cell
                                dead_surrounding_live += 1

                                # Adds to counter for this dead cell
                                if coord in live_surrounding_dead:
                                    live_surrounding_dead[coord] += 1
                                else:
                                    live_surrounding_dead[coord] = 1
                        else:
                            dead_surrounding_live += 1

                    # Makes the cell die if it doesn't have the right amount of
                    # live neighbors
                    if 8 - dead_surrounding_live not in [2, 3]:
                        make_dead.append(cell)

                # Makes the according cells dead
                for coord in make_dead:
                    if coord in self.__live_cells:
                        self.__live_cells.remove(coord)
                        self.__universe[coord[0]][coord[1]].switch_state(CellState.DEAD)

                # Makes the according cells live
                for coord, counter in live_surrounding_dead.items():
                    if counter == 3 and in_bounds(coord):
                        self.__universe[coord[0]][coord[1]].switch_state(CellState.LIVE)
                        self.__live_cells.add(coord)
            
                # Stops the universe from updating further if the it's stagnant
                if self.__prev_universe_states == self.__universe:
                    self.__stop_button.set_is_pressed(True)
                    self.__is_active = False
                    self.__play_button.set_is_pressed(False)
                else:
                    self.__prev_universe_states = self.__generate_universe_states()

    def __click_cell(self, x: int, y: int) -> None:
        """Event handler for a mouse press or drag on a cell."""
        col = y//20
        row = x//20
        if self.__click_action == CellState.LIVE:
            self.__live_cells.add((col, row))
        else:
            if (col, row) in self.__live_cells:
                self.__live_cells.remove((col,row))
        self.__universe[col][row].switch_state(self.__click_action)
    
    def __generate_universe(self) -> list[tuple[Cell]]:
        """Return an array of all the cells in the universe, starting dead."""
        universe = []
        for y_cor in range(0, 640, 20):
            universe.append([])
            for x_cor in range(0, 640, 20):
                universe[-1].append(Cell(y_cor, x_cor, self.__main_batch, self.__cell_group))
        return universe

    def __generate_universe_states(self) -> list[list[CellState]]:
        """
        Return an array of CellStates corresponding to the universe: an array
        of all the cells.
        """
        return [[cell.state for cell in row] for row in self.__universe]

    def __reset_scene(self) -> None:
        """Reset the object's changed attributes to their default values."""
        self.__play_button.set_is_pressed(False)
        self.__stop_button.set_is_pressed(True)
        self.__is_active = False
        self.__live_button.set_is_pressed(True)
        self.__dead_button.set_is_pressed(False)
        self.__pause_panel.set_is_showing(False)
        self.__click_action = CellState.LIVE
        self.__universe = self.__generate_universe()
        self.__live_cells = set()