from model.Input import Input


class InputsContainer:
    def __init__(self):
        self.Inputs: dict[str, Input] = {}

    def __str__(self):
        return '\n'.join([f"\t{input} = {input.value}" for input in self.Inputs.values()])
