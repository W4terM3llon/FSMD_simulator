from fsmdSim.DataReader import DataReader
from model.Condition import Condition
from model.ConditionsContainer import ConditionsContainer
from model.Input import Input
from model.InputsContainer import InputsContainer
from model.Instruction import Instruction
from model.InstructionsContainer import InstructionsContainer
from model.State import State
from model.StatesContainer import StatesContainer
from model.Transition import Transition
from model.TransitionsContainer import TransitionsContainer
from model.Variable import Variable
from model.VariablesContainer import VariablesContainer
from services.InputStimuliExecutor import InputStimuliExecutor
from services.Logger import Logger
from services.TransitionsExecutor import TransitionsExecutor
from services.DynamicExpressionExecutor import DynamicExpressionExecutor

'''
Instances which are injected into constructors - dependency inversion by injection 
'''
maxCycleCount, statesContainer, variablesContainer, inputsContainer, instructionsContainer, conditionsContainer, transitionsContainer, inputStimuliContainer = DataReader().readDescriptionData()
variableExpressionExecutor = DynamicExpressionExecutor(variablesContainer)
#inputStimuliExpressionExecutor = DynamicExpressionExecutorABC(inputStimuliContainer)
transitionsExecutor = TransitionsExecutor(transitionsContainer, statesContainer, variableExpressionExecutor)
#inputStimuliExecutor = InputStimuliExecutor(inputStimuliContainer, variableExpressionExecutor)
logger = Logger(statesContainer, variablesContainer)
