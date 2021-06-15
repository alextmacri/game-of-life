import pyglet
# from game_of_life.ModeController import ModeController
# from game_of_life.SceneController import SceneController

class SceneInterface:
    """"""

    def __init__(self, parent_scene_controller) -> None:
        self.active = None(bool)
        self.parent_scene_controller = None

        self.main_batch = None(pyglet.graphics.Batch)
    
    def mouse_press(self, x: int, y: int, button: int):
        """Accounts for the event of a mouse press"""
        pass

    def mouse_release(self, x: int, y: int, button: int):
        """Accounts for the event of a mouse release"""
        pass

    def draw(self):
        """Drawing the Scene"""
        pass