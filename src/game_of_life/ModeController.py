from game_of_life.ModeState import ModeState
from game_of_life.SceneController import SceneController
from game_of_life.scenes.Menu import Menu
from game_of_life.scenes.Free import Free
from game_of_life.scenes.Target import Target

class ModeController:
    def __init__(self):
        self.modes = {
            ModeState.MENU: SceneController(
                self,
                {'menu': Menu},
                'menu'
            ),
            ModeState.FREE: SceneController(
                self,
                {'free': Free},
                'free'
            ),
            ModeState.TARGET: SceneController(
                self,
                {'target': Target},
                'target'
            )
        }

        self.active_mode = self.modes[ModeState.MENU]

    def switch_mode(self, mode_state: ModeState):
        self.active_mode = self.modes[mode_state]