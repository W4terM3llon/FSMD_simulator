from model.DynamicExpressionABC import DynamicExpression


class Condition(DynamicExpression):
    def __init__(self, name: str, dynamicExpression: str):
        super().__init__(dynamicExpression)
        self.name: str = name