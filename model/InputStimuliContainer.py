from model.InputStimulus import InputStimulus


class InputStimuliContainer:
    def __init__(self):
        self.objects: dict[int, InputStimulus] = {}
