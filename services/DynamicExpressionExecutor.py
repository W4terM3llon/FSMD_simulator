class DynamicExpressionExecutor:
    def __init__(self, variablesContainer, inputsContainer):
        self.variablesContainer = variablesContainer
        self.inputsContainer = inputsContainer

    def executeDynamicExpression(self, dynamicExpression: str, shouldReturn: bool):
        adjustedDynamicExpression = self._replaceAllRawVariableOccurrences(dynamicExpression)

        if shouldReturn:
            return eval(adjustedDynamicExpression)  # super unsafe but simple af
        else:
            exec(adjustedDynamicExpression)  # super unsafe but simple af

    def _replaceAllRawVariableOccurrences(self, dynamicExpression):
        dynamicExpressionLines = dynamicExpression.split('\n')
        for j in range(0, len(dynamicExpressionLines)):
            expressionWords = dynamicExpressionLines[j].split(' ')
            for i in range(0, len(expressionWords)):
                match expressionWords[i].split('_')[0].lower():
                    case 'var':
                        if expressionWords[i] in self.variablesContainer.objects:
                            expressionWords[i] = self._getAdjustedVariableName(expressionWords[i])
                        else:
                            raise Exception(F"Variable '{expressionWords[i]}' was not defined in Variables.")
                    case 'in':
                        if expressionWords[i] in self.inputsContainer.objects:
                            expressionWords[i] = self._getAdjustedInputName(expressionWords[i])
                        else:
                            raise Exception(F"Input '{expressionWords[i]}' was not defined in Inputs.")
            dynamicExpressionLines[j] = ' '.join(expressionWords)
        adjustedCondition = '\n'.join(dynamicExpressionLines)

        return adjustedCondition

    def _getAdjustedVariableName(self, rawName):
        return f"self.variablesContainer.objects['{rawName}'].value"

    def _getAdjustedInputName(self, rawName):
        return f"self.inputsContainer.objects['{rawName}'].value"
