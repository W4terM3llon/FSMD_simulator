from model.Condition import Condition


class ConditionsContainer:
    def __init__(self):
        self.Conditions: dict[str, Condition] = {
            "True": Condition("True", "True"),
            "False": Condition("False", "False")}
