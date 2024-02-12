class DynamicExpressionExecutor:
    def __init__(self, dynamicExpressionsContainer):
        self.dynamicExpressionsContainer = dynamicExpressionsContainer

    def executeDynamicExpression(self, dynamicExpression: str, shouldReturn: bool):
        adjustedDynamicExpression = self._replaceAllRawVariableOccurrences(dynamicExpression)

        if shouldReturn:
            return eval(adjustedDynamicExpression)  # super unsafe but simple af
        else:
            exec(adjustedDynamicExpression)  # super unsafe but simple af

    def _replaceAllRawVariableOccurrences(self, dynamicExpression):
        expressionWords = dynamicExpression.split(' ')
        for i in range(0, len(expressionWords)):
            if expressionWords[i] in self.dynamicExpressionsContainer.objects:
                expressionWords[i] = self._getAdjustedVariableName(expressionWords[i])
        adjustedCondition = ' '.join(expressionWords)

        return adjustedCondition

    def _getAdjustedVariableName(self, rawName):
        return f"self.dynamicExpressionsContainer.objects['{rawName}'].dynamicExpression"
