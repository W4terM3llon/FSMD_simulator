from model.InputStimuliContainer import InputStimuliContainer
from services.DynamicExpressionExecutor import DynamicExpressionExecutor


class InputStimuliExecutor:
    def __init__(self, inputStimuliContainer, variableExpressionExecutor):
        self.inputStimuliContainer: InputStimuliContainer = inputStimuliContainer
        self.inputStimuliExpressionExecutor: DynamicExpressionExecutor = variableExpressionExecutor

    def executeInputStimuli(self, cycle):
        inputStimuli = self.inputStimuliContainer.objects[cycle]
        if inputStimuli is not None:
            for expression in inputStimuli.dynamicExpression:
                self.inputStimuliExpressionExecutor.executeDynamicExpression(expression, False)
