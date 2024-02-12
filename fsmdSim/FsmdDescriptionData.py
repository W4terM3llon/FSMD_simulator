class FsmdDescriptionData:
    def __init__(self, states: list[str], initialState: str, inputs: dict[str, float], variables: dict[str, float], operations: dict[str, str], conditions: dict[str, str], fsmdTransitions: dict[str, list[dict[str, str]]]):
        self.states: list[str] = states
        self.initialState: str = initialState
        self.inputs: dict[str, float] = inputs
        self.variables: dict[str, float] = variables
        self.operations: dict[str, str] = operations
        self.conditions: dict[str, str] = conditions
        self.fsmdTransitionsByStatus: dict[str, list[dict[str, str]]] = fsmdTransitions