from typing import Callable
from game_of_life.ModeState import ModeState
from game_of_life.SceneInterface import SceneInterface

class SceneController:
    """
    Represents a mode, or holder and controller of scenes in the game.

    switch_mode_cb: Callable[[ModeState], None], the callable function from
    GameWindow to switch modes
    """

    def __init__(self, switch_mode_cb: Callable[[ModeState], None],
                 scenes: dict[str, SceneInterface], active_scene: str):
        """Initialize this Button."""
        # Initializing each SceneInterface object that was passed in, so I can
        # pass in the callbacks
        for scene_key in scenes:
            scenes[scene_key] = scenes[scene_key](
                self.__switch_scene,
                switch_mode_cb
            )
        self.scenes = scenes
        self.__switch_scene(active_scene)
    
    def __switch_scene(self, scene_name: str):
        """
        Switch the current scene to the scene of scene_state by updating the
        active scene.
        """
        self.active_scene = self.scenes[scene_name]