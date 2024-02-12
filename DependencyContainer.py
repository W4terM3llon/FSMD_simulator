from fsmdSim.DataReader import DataReader
from services.InputStimuliExecutor import InputStimuliExecutor
from services.Logger import Logger
from services.TransitionsExecutor import TransitionsExecutor
from services.DynamicExpressionExecutor import DynamicExpressionExecutor


statesContainer, variablesContainer, inputsContainer, instructionsContainer, conditionsContainer, transitionsContainer, inputStimuliContainer, programState = DataReader().readDescriptionData()
variableExpressionExecutor = DynamicExpressionExecutor(variablesContainer, inputsContainer)
transitionsExecutor = TransitionsExecutor(transitionsContainer, variableExpressionExecutor, programState)
inputStimuliExecutor = InputStimuliExecutor(inputStimuliContainer, variableExpressionExecutor)
logger = Logger(statesContainer, variablesContainer, inputsContainer, programState)