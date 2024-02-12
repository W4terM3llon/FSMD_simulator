from model.Input import Input


class InputsContainer:
    def __init__(self):
        self.objects: dict[str, Input] = {}

    def __str__(self):
        return '\n'.join([f"\t{input.name} = {input.value}" for input in self.objects.values()])
