from model.State import State


class StatesContainer:
    def __init__(self, initialState: State):
        self.states: dict[State] = {}
        self.currentState: State = initialState