from abc import ABC


class DynamicExpression(ABC):
    def __init__(self, dynamicExpression: str):
        self.dynamicExpression: str = dynamicExpression