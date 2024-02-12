from model.Instruction import Instruction


class InstructionsContainer:
    def __init__(self):
        self.Instructions: dict[str, Instruction] = {
            "NOP": Instruction("NOP", ""),
            "-": Instruction("-", "")}

    def __str__(self):
        return '\n'.join([f'\t{instruction.name}' for instruction in self.Instructions.values()])