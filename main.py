from DependencyContainer import transitionsExecutor, logger, variablesContainer, programState , inputStimuliExecutor
from model.VariablesContainer import VariablesContainer
from services.InputStimuliExecutor import InputStimuliExecutor
from services.Logger import Logger
from services.TransitionsExecutor import TransitionsExecutor


class Program:
    def __init__(self, transitionsExecutor, inputStimuliExecutor, logger, variablesContainer, programState):
        self.transitionsExecutor: TransitionsExecutor = transitionsExecutor
        self.inputStimuliExecutor: InputStimuliExecutor = inputStimuliExecutor
        self.logger: Logger = logger
        self.variablesContainer: VariablesContainer = variablesContainer
        self.programState = programState

    def run(self):
        self.logger.logStart()
        cycleCounter = 0
        while cycleCounter <= self.programState.maxCycleCount and self.programState.finishState != self.programState.currentState:
            self.inputStimuliExecutor.executeInputStimuli(cycleCounter)
            transition = self.transitionsExecutor.executeTransitions()
            self.logger.logCycle(cycleCounter, transition)
            cycleCounter += 1

        # Print last state
        transition = self.transitionsExecutor.executeTransitions()
        self.logger.logCycle(cycleCounter, transition)

        self.logger.logEnd()


if __name__ == "__main__":
    program = Program(transitionsExecutor, inputStimuliExecutor, logger, variablesContainer, programState)
    program.run()
