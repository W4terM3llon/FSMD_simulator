from model.StatesContainer import StatesContainer
from model.Transition import Transition
from model.TransitionsContainer import TransitionsContainer
from services.DynamicExpressionExecutor import DynamicExpressionExecutor


class TransitionsExecutor:
    def __init__(self, transitionsContainer, statesContainer, variableExpressionExecutor):
        self.transitionsContainer: TransitionsContainer = transitionsContainer
        self.statesContainer: StatesContainer = statesContainer
        self.variableExpressionExecutor: DynamicExpressionExecutor = variableExpressionExecutor

    def executeTransitions(self) -> Transition:
        for transition in self.transitionsContainer.Transitions[self.statesContainer.currentState]:
            if self.variableExpressionExecutor.executeDynamicExpression(transition.condition.dynamicExpression, True):
                for instruction in transition.instructions:
                    print(instruction.instruction)
                    self.variableExpressionExecutor.executeDynamicExpression(instruction.instruction, False)
                self.updateState(transition.nextState)
                return transition

        raise Exception("Exactly one transition has to be executed.")

    def updateState(self, nextState):
        self.statesContainer.currentState = nextState
