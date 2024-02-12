from model.State import State
from model.Transition import Transition


class TransitionsContainer:
    def __init__(self):
        self.Transitions: dict[State, list[Transition]] = {}
