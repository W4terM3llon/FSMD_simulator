from DependencyContainer import maxCycleCount, transitionsExecutor, logger, variablesContainer#, inputStimuliExecutor
from model.VariablesContainer import VariablesContainer
from services.InputStimuliExecutor import InputStimuliExecutor
from services.Logger import Logger
from services.TransitionsExecutor import TransitionsExecutor


class Program:
    def __init__(self, maxCycleCount, transitionsExecutor, inputStimuliExecutor, logger, variablesContainer):
        self.maxCycleCount: int = maxCycleCount
        self.transitionsExecutor: TransitionsExecutor = transitionsExecutor
        self.inputStimuliExecutor: InputStimuliExecutor = inputStimuliExecutor
        self.logger: Logger = logger
        self.variablesContainer: VariablesContainer = variablesContainer

    def run(self):
        self.logger.logStart()
        cycleCounter = 0
        while cycleCounter <= self.maxCycleCount:
            transition = self.transitionsExecutor.executeTransitions()
            #self.inputStimuliExecutor.executeInputStimuli(cycleCounter)
            self.logger.logCycle(cycleCounter, transition)
            cycleCounter += 1
        self.logger.logEnd()


if __name__ == "__main__":
    program = Program(maxCycleCount, transitionsExecutor, None, logger, variablesContainer)
    program.run()
