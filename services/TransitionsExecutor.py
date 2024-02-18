from fsmdSim.ProgramState import ProgramState
from model.StatesContainer import StatesContainer
from model.Transition import Transition
from model.TransitionsContainer import TransitionsContainer
from services.DynamicExpressionExecutor import DynamicExpressionExecutor


class TransitionsExecutor:
    def __init__(self, transitionsContainer, variableExpressionExecutor, programState):
        self.transitionsContainer: TransitionsContainer = transitionsContainer
        self.variableExpressionExecutor: DynamicExpressionExecutor = variableExpressionExecutor
        self.programState: ProgramState = programState

    def executeTransitions(self) -> Transition:
        for transition in self.transitionsContainer.Transitions[self.programState.currentState]:
            if self.variableExpressionExecutor.executeDynamicExpression(transition.condition.dynamicExpression, True):
                for instruction in transition.instructions:
                    self.variableExpressionExecutor.executeDynamicExpression(instruction.instruction, False)
                self.updateState(transition.nextState)
                return transition

        raise Exception("Exactly one transition has to be executed.")

    def updateState(self, nextState):
        self.programState.currentState = nextState
