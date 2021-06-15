from game_of_life.SceneInterface import SceneInterface

class SceneController:
    def __init__(self, parent_mode_controller, scenes: dict[str, SceneInterface], active: str):
        self.parent_mode_controller = parent_mode_controller

        for scene_key in scenes:
            scenes[scene_key] = scenes[scene_key](self)

        self.scenes = scenes

        self.active_scene = self.scenes[active]
    
    def switch_scene(self, scene_name: str):
        self.active_scene = self.scenes[scene_name]