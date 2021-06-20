import pyglet
from game_of_life.CellState import CellState
from game_of_life.assets import cell_dead_image, cell_live_image

class Cell:
    """
    Represents a cell in a Game of Life universe.

    state: CellState, the state of the cell
    y_cor: int, the y coordinates of the bottom of the cell when drawn in the
    game window
    x_cor: int, the x coordinates of the left of the cell when drawn in the game
    window
    batch: pyglet.graphics.Batch, the pyglet rendering batch that the cell's
    sprite belongs to
    group: pyglet.graphics.OrderedGroup, the pyglet rendering group that the
    cell's sprite belongs to
    images: dict[CellState, pyglet.image.ImageData], the images that a cell uses
    in each state
    sprite: pyglet.sprite.Sprite, the current sprite of the cell
    """

    def __init__(self, y_cor: int, x_cor: int, batch: pyglet.graphics.Batch,
                 group: pyglet.graphics.OrderedGroup) -> None:
        """Initialize this Cell."""
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
    
    def switch_state(self, cell_state: CellState) -> None:
        """Switch the current state to cell_state and update the sprite."""
        self.state = cell_state
        self.update_sprite()

    def __define_sprite(self) -> pyglet.sprite.Sprite:
        """Define the sprite, using the other class attributes."""
        return pyglet.sprite.Sprite(
            # Uses cell_dead_image if dead, and cell_live_image if live
            self.__images[self.state],
            x=self.__x_cor,
            y=self.__y_cor,
            batch=self.__batch,
            group=self.__group
        )

    def update_sprite(self) -> None:
        """Delete the current sprite, and make a new one in its place."""
        self.__sprite.delete()
        self.__sprite = self.__define_sprite()

    def __repr__(self) -> str:
        """Return string representation of Cell's state."""
        return 'DEAD' if self.state == CellState.DEAD else 'LIVE'
    
    def __eq__(self, o: object) -> bool:
        """
        Return the result of a comparison of this Cell to another Cell or to a
        seperate state.
        """
        if isinstance(o, type(self)):
            # Doing a basic comparison if the object is the same type
            return self.state == o.state
        elif isinstance(o, type(CellState.LIVE)):
            # Doing a comparison with the state if the object is a state
            return self.state == o
        return False