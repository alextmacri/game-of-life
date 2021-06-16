from typing import Callable
from game_of_life.ModeState import ModeState
from game_of_life.SceneInterface import SceneInterface

class SceneController:
    def __init__(self, switch_mode_cb: Callable[[ModeState], None], scenes: dict[str, SceneInterface], active_scene: str):
        self.__switch_mode_cb = switch_mode_cb

        for scene_key in scenes:
            scenes[scene_key] = scenes[scene_key](self.__switch_scene, self.__switch_mode_cb)
        self.scenes = scenes
        self.__switch_scene(active_scene)
    
    def __switch_scene(self, scene_name: str):
        self.active_scene = self.scenes[scene_name]
        self.active_scene.set_is_active(True)