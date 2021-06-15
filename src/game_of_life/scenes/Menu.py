import pyglet
from game_of_life.ModeState import ModeState
# from game_of_life.ModeController import ModeController
# from game_of_life.SceneController import SceneController
from game_of_life.SceneInterface import SceneInterface

class Menu(SceneInterface):
    def __init__(self, parent_scene_controller) -> None:
        self.active = None
        self.parent_scene_controller = parent_scene_controller

        self.main_batch = pyglet.graphics.Batch()
        self.thing = 'menu'
    
    def mouse_press(self, x: int, y: int, button: int):
        """Accounts for the event of a mouse press"""
        print('switched')
        self.parent_scene_controller.parent_mode_controller.switch_mode(ModeState.TARGET)

    def mouse_release(self, x: int, y: int, button: int):
        """Accounts for the event of a mouse release"""
        pass

    def draw(self):
        """Drawing the Scene"""
        pass

    def update(dt: float):
        """Updating the scene after the previously specified interval"""
        pass