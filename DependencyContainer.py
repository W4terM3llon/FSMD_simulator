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
Converts raw data read by DataReader to instances of classes defined in Model package
'''
def CreateDTOObjects():
    maxCycleCount, initialState, states, inputs, variables, operations, conditions, fsmdTransitions = DataReader().readDescriptionData()
    inputStimuliContainer = []#DataReader().readStimuliData()

    stateObjects = {}
    for state in states:
        stateObjects[state] = State(state)
    statesContainer = StatesContainer(stateObjects[initialState])
    statesContainer.states = stateObjects

    variablesContainer = VariablesContainer()
    for (name, value) in variables.items():
        variablesContainer.objects[name] = Variable(name, value)

    inputsContainer = InputsContainer()
    for (name, value) in inputs.items():
        inputsContainer.objects[name] = Input(name, value)

    instructionsContainer = InstructionsContainer()
    for (name, value) in operations.items():
        instructionsContainer.Instructions[name] = Instruction(name, value)

    conditionsContainer = ConditionsContainer()
    for (name, value) in conditions.items():
        conditionsContainer.Conditions[name] = Condition(name, value)

    transitionsContainer = TransitionsContainer()
    for (stateName, rawTransitions) in fsmdTransitions.items():
        state = statesContainer.states[stateName]

        transitions = []
        for transition in rawTransitions:
            nextStateName = transition["nextstate"]
            conditionName = transition["condition"]
            instructionsNames = transition["instruction"].strip().split(' ')
            transitions.append(
                Transition(
                    state,
                    statesContainer.states[nextStateName],
                    conditionsContainer.Conditions[conditionName],
                    [instructionsContainer.Instructions[instructionName] for instructionName in instructionsNames]))
        transitionsContainer.Transitions[state] = transitions

    return maxCycleCount, statesContainer, variablesContainer, inputsContainer, instructionsContainer, conditionsContainer, transitionsContainer, inputStimuliContainer


'''
Instances which are injected into constructors - dependency inversion by injection 
'''
maxCycleCount, statesContainer, variablesContainer, inputsContainer, instructionsContainer, conditionsContainer, transitionsContainer, inputStimuliContainer = CreateDTOObjects()
variableExpressionExecutor = DynamicExpressionExecutor(variablesContainer, inputsContainer)
#inputStimuliExpressionExecutor = DynamicExpressionExecutorABC(inputStimuliContainer)
transitionsExecutor = TransitionsExecutor(transitionsContainer, statesContainer, variableExpressionExecutor)
#inputStimuliExecutor = InputStimuliExecutor(inputStimuliContainer, variableExpressionExecutor)
logger = Logger(statesContainer, variablesContainer, inputsContainer)
