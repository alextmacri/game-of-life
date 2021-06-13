from game_of_life.SceneInterface import SceneInterface
from game_of_life.ModeController import ModeController

class SceneController:
    def __init__(self, parent_mode_controller: ModeController, scenes: dict[str, SceneInterface], active: str):
        self.__parent_mode_controller = parent_mode_controller
        self.scenes = scenes
        self.active_scene = scenes[active]
    
    def switch_scene(self, scene_name: str):
        self.active_scene = self.scenes[scene_name]