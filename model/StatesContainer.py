from model.State import State


class StatesContainer:
    def __init__(self):
        self.states: dict[State] = {}