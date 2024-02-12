from fsmdSim.ProgramState import ProgramState
from model.StatesContainer import StatesContainer
from model.Transition import Transition
from model.VariablesContainer import VariablesContainer


class Logger():
    def __init__(self, statesContainer, variablesContainer, inputsContainer, programState):
        self.inputsContainer = inputsContainer
        self.statesContainer: StatesContainer = statesContainer
        self.variablesContainer: VariablesContainer = variablesContainer
        self.programState: ProgramState = programState

    def logMessage(self, message):
        print(message)

    def logStart(self):
        self.logMessage(f"""
---Start simulation---
At the beginning of the simulation the status is:
Variables:
{self.variablesContainer}
Initial state: {self.programState.currentState.name}""")

    def logCycle(self, cycle: int, transition: Transition):
        self.logMessage(f"""
--------------------------------------------------
Cycle: {cycle}
Current state: {transition.state.name}
Inputs: 
{self.inputsContainer}
The condition ({transition.condition.name}) is true.
Executing instruction(s): 
{str(chr(10)).join([f'{chr(9)}{instruction.name}' for instruction in transition.instructions])}
Next state: {transition.nextState.name}
At the end of cycle {cycle} execution, the status is:
Variables:
{self.variablesContainer}""")

    def logEnd(self):
        self.logMessage(f"""
--------------------------------------------------
End-state reached.
End of simulation. Goodbye!""")