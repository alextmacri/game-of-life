from game_of_life.ModeState import ModeState
from game_of_life.Mode import Mode

class ModeController:
    def __init__(self, modes: dict[ModeState, Mode], active: ModeState):
        self.modes = modes
        self.active_mode = self.modes[active]

    def switch_mode(self, mode_state: ModeState):
        self.active_mode = self.modes[mode_state]