from model import Instruction
from model.Condition import Condition
from model.State import State


class Transition:
    def __init__(self, state: State, nextState: State, condition: Condition, instructions: list[Instruction]):
        self.state: State = state
        self.nextState: State = nextState
        self.condition: Condition = condition
        self.instructions: list[Instruction] = instructions