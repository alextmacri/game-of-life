from game_of_life.ModeController import ModeController
from game_of_life.SceneController import SceneController

class Mode:
    def __init__(self, parent_mode_controller: ModeController,
                 scene_controller: SceneController):
        self.parent_mode_controller = parent_mode_controller
        self.scene_controller = scene_controller