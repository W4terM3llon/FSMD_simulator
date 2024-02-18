from model.State import State


class ProgramState:
    def __init__(self, initialState, maxCycleCount, finishState):
        self.currentState: State = initialState
        self.maxCycleCount: int = maxCycleCount
        self.finishState: State = finishState