from model.InputStimuliContainer import InputStimuliContainer
from services.DynamicExpressionExecutor import DynamicExpressionExecutor


class InputStimuliExecutor:
    def __init__(self, inputStimuliContainer, variableExpressionExecutor):
        self.inputStimuliContainer: InputStimuliContainer = inputStimuliContainer
        self.inputStimuliExpressionExecutor: DynamicExpressionExecutor = variableExpressionExecutor

    def executeInputStimuli(self, cycle):
        if cycle not in self.inputStimuliContainer.objects:
            return

        inputStimuli = self.inputStimuliContainer.objects[cycle]
        self.inputStimuliExpressionExecutor.executeDynamicExpression(inputStimuli.dynamicExpression, False)
