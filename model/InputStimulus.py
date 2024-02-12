from model.DynamicExpressionABC import DynamicExpression


class InputStimulus(DynamicExpression):
    def __init__(self, cycle: int, dynamicExpression: str):
        super().__init__(dynamicExpression)
        self.cycle: int = cycle