class ProgramState:
    def __init__(self, initialState, maxCycleCount):
        self.state = initialState
        self.maxCycleCount = maxCycleCount