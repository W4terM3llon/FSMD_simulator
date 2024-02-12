from model.Variable import Variable


class VariablesContainer:
    def __init__(self):
        self.objects: dict[str, Variable] = {}

    def __str__(self):
        return '\n'.join([f"\t{variable.name} = {variable.value}" for variable in self.objects.values()])
