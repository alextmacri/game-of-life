import pyglet
from game_of_life.CellState import CellState
from game_of_life.assets import cell_dead_image, cell_live_image

class Cell:
    def __init__(self, y_pos, x_pos):
        self.state = CellState.DEAD

        self.y_pos = y_pos
        self.x_pos = x_pos

        self.__sprites = {
            CellState.DEAD: cell_dead_image,
            CellState.LIVE: cell_live_image
        }
        self.active_sprite = self.__sprites[CellState.DEAD]
    
    def switch_state(self, state: CellState):
        self.state = state
        self.active_sprite = self.__sprites[state]