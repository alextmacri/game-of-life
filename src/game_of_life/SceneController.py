from game_of_life.SceneInterface import SceneInterface

class SceneController:
    def __init__(self, scenes: dict[str, SceneInterface], active: str):
        self.scenes = scenes
        self.active_scene = scenes[active]
    
    def switch_scene(self, scene_name: str):
        self.active_scene = self.scenes[scene_name]