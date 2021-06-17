import pyglet
from game_of_life.CellState import CellState
from game_of_life.assets import cell_dead_image, cell_live_image

class Cell:
    """
    Represents a Game of Life cell in the universe

    state: CellState
    y_
    """

    def __init__(self, y_cor: int, x_cor: int, batch: pyglet.graphics.Batch,
                 group: pyglet.graphics.OrderedGroup) -> None:
        self.state = CellState.DEAD

        self.__y_cor = y_cor
        self.__x_cor = x_cor

        self.__batch = batch
        self.__group = group

        self.__images = {
            CellState.DEAD: cell_dead_image,
            CellState.LIVE: cell_live_image
        }
        
        self.__sprite = self.__define_sprite()
    
    def switch_state(self, state: CellState):
        """Switches state (and according sprite) of the cell"""
        self.state = state
        self.update_sprite()

    def __define_sprite(self) -> pyglet.sprite.Sprite:
        return pyglet.sprite.Sprite(
            self.__images[self.state],
            x=self.__x_cor,
            y=self.__y_cor,
            batch=self.__batch,
            group=self.__group
        )

    def update_sprite(self):
        self.__sprite.delete()
        self.__sprite = self.__define_sprite()

    def __repr__(self) -> str:
        return 'DEAD' if self.state == CellState.DEAD else 'LIVE'
    
    def __eq__(self, o: object) -> bool:
        if isinstance(o, type(self)):
            return self.state == o.state
        elif isinstance(o, type(CellState.LIVE)):
            return self.state == o
        return False