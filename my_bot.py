from poker_game_runner.state import Observation

BOT_NAME = "Mus"

class Bot:
    @classmethod
    def get_name_class(cls, path):
        return BOT_NAME

    def get_name(self):
        return BOT_NAME

    def act(self, obs: Observation):
        if self.is_logical_to_raise(obs):
            if obs.get_my_hand_type().value > 3:
                return obs.get_max_raise()
            else:
                return obs.get_min_raise()
        else:
            return self.check_fold(obs)

    def is_logical_to_raise(self, obs: Observation):
        return obs.get_my_hand_type().value > obs.get_board_hand_type().value

    def has_anyone_raised(self, obs: Observation):
        return obs.get_call_size() > obs.get_min_raise()

    def check_fold(self, obs: Observation):
        return 0 if self.has_anyone_raised(obs) else 1