import sys
import xmltodict

from model.Condition import Condition
from model.ConditionsContainer import ConditionsContainer
from model.Input import Input
from model.InputStimuliContainer import InputStimuliContainer
from model.InputStimulus import InputStimulus
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



class DataReader:
    def readDescriptionData(self):
        print("Welcome to the FSMD simulator! - Version ?? - Designed by ??")

        if len(sys.argv) < 3:
            print('Too few arguments.')
            sys.exit(-1)
        elif (len(sys.argv) > 4):
            print('Too many arguments.')
            sys.exit(-1)

        iterations = int(sys.argv[1])

        # Parsing the FSMD description file
        with open(sys.argv[2]) as fd:
            fsmd_des = xmltodict.parse(fd.read())

        print("\n--FSMD description--")

        inputStimuliContainer = []#DataReader().readStimuliData()
        
        states = self.__ReadStates(fsmd_des)
        initialState = self.__ReadInitialState(fsmd_des)
        inputs = self.__ReadInputs(fsmd_des)
        variables = self.__ReadVariables(fsmd_des)
        operations = self.__ReadOperations(fsmd_des)
        conditions = self.__ReadConditions(fsmd_des)
        fsmdTransitions = self.__ReadFsmdTransitions(fsmd_des, states)


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
            inputsContainer.Inputs[name] = Input(name, value)

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

    
        return iterations, statesContainer, variablesContainer, inputsContainer, instructionsContainer, conditionsContainer, transitionsContainer, inputStimuliContainer


    def readStimuliData(self) -> InputStimuliContainer:
        if len(sys.argv) < 3:
            print('Too few arguments.')
            sys.exit(-1)
        elif (len(sys.argv) > 4):
            print('Too many arguments.')
            sys.exit(-1)

        # Parsing the stimuli file
        fsmd_stim = {}
        if len(sys.argv) == 4:
            with open(sys.argv[3]) as fd:
                fsmd_stim = xmltodict.parse(fd.read())

        dynamicExpressionByCycle = {}
        if (not(fsmd_stim['fsmdstimulus']['setinput'] is None)):
            for setinput in fsmd_stim['fsmdstimulus']['setinput']:
                cycle = int(setinput['cycle'])
                expression = setinput['expression']
                if cycle in dynamicExpressionByCycle:
                    dynamicExpressionByCycle[cycle].append(expression)
                else:
                    dynamicExpressionByCycle[cycle] = [expression]

        inputStimuliContainer = InputStimuliContainer()
        for (cycle, expressions) in dynamicExpressionByCycle.items():
            inputStimuliContainer.objects[cycle] = InputStimulus(cycle, '\n'.join(expressions))

        return inputStimuliContainer

    def __ReadStates(self, fsmd_des):
        #
        # Description:
        # The 'states' variable of type 'list' contains the list of all states names.
        #
        states = fsmd_des['fsmddescription']['statelist']['state']
        print("States:")
        for state in states:
            print('  ' + state)
        return states

    def __ReadInitialState(self, fsmd_des):
        #
        # Description:
        # The 'initial_state' variable of type 'string' contains the initial_state name.
        #
        initial_state = fsmd_des['fsmddescription']['initialstate']
        print("Initial state:")
        print('  ' + initial_state)
        return initial_state

    def __ReadInputs(self, fsmd_des):
        #
        # Description:
        # The 'inputs' variable of type 'dictionary' contains the list of all inputs
        # names and value. The default value is 0.
        #
        inputs = {}
        if (fsmd_des['fsmddescription']['inputlist'] is None):
            inputs = {}
            # No elements
        else:
            if type(fsmd_des['fsmddescription']['inputlist']['input']) is str:
                # One element
                inputs[fsmd_des['fsmddescription']['inputlist']['input']] = 0
            else:
                # More elements
                for input_i in fsmd_des['fsmddescription']['inputlist']['input']:
                    inputs[input_i] = 0
        print("Inputs:")
        for input_i in inputs:
            print('  ' + input_i)
        return inputs

    def __ReadVariables(self, fsmd_des):
        #
        # Description:
        # The 'variables' variable of type 'dictionary' contains the list of all variables
        # names and value. The default value is 0.
        #
        variables = {}
        if (fsmd_des['fsmddescription']['variablelist'] is None):
            variables = {}
            # No elements
        else:
            if type(fsmd_des['fsmddescription']['variablelist']['variable']) is str:
                # One element
                variables[fsmd_des['fsmddescription']['variablelist']['variable']] = 0
            else:
                # More elements
                for variable in fsmd_des['fsmddescription']['variablelist']['variable']:
                    variables[variable] = 0
        print("Variables:")
        for variable in variables:
            print('  ' + variable)
        return variables

    def __ReadOperations(self, fsmd_des):
        #
        # Description:
        # The 'operations' variable of type 'dictionary' contains the list of all the
        # defined operations names and expressions.
        #
        operations = {}
        if (fsmd_des['fsmddescription']['operationlist'] is None):
            operations = {}
            # No elements
        else:
            for operation in fsmd_des['fsmddescription']['operationlist']['operation']:
                if type(operation) is str:
                    # Only one element
                    operations[fsmd_des['fsmddescription']['operationlist']['operation']['name']] = \
                        fsmd_des['fsmddescription']['operationlist']['operation']['expression']
                    break
                else:
                    # More than 1 element
                    operations[operation['name']] = operation['expression']
        print("Operations:")
        for operation in operations:
            print('  ' + operation + ' : ' + operations[operation])
        return operations

    def __ReadConditions(self, fsmd_des):
        #
        # Description:
        # The 'conditions' variable of type 'dictionary' contains the list of all the
        # defined conditions names and expressions.
        #
        conditions = {}
        if (fsmd_des['fsmddescription']['conditionlist'] is None):
            conditions = {}
            # No elements
        else:
            for condition in fsmd_des['fsmddescription']['conditionlist']['condition']:
                if type(condition) is str:
                    # Only one element
                    conditions[fsmd_des['fsmddescription']['conditionlist']['condition']['name']] = \
                        fsmd_des['fsmddescription']['conditionlist']['condition']['expression']
                    break
                else:
                    # More than 1 element
                    conditions[condition['name']] = condition['expression']
        print("Conditions:")
        for condition in conditions:
            print('  ' + condition + ' : ' + conditions[condition])
        return conditions

    def __ReadFsmdTransitions(self, fsmd_des, states):
        #
        # Description:
        # The 'fsmd' variable of type 'dictionary' contains the list of dictionaries,
        # one per state, with the fields 'condition', 'instruction', and 'nextstate'
        # describing the FSMD transition table.
        #
        fsmd = {}
        for state in states:
            fsmd[state] = []
            for transition in fsmd_des['fsmddescription']['fsmd'][state]['transition']:
                if type(transition) is str:
                    # Only one element
                    fsmd[state].append({'condition': fsmd_des['fsmddescription']['fsmd'][state]['transition']['condition'],
                                        'instruction': fsmd_des['fsmddescription']['fsmd'][state]['transition'][
                                            'instruction'],
                                        'nextstate': fsmd_des['fsmddescription']['fsmd'][state]['transition']['nextstate']})
                    break
                else:
                    # More than 1 element
                    fsmd[state].append({'condition': transition['condition'],
                                        'instruction': transition['instruction'],
                                        'nextstate': transition['nextstate']})
        print("FSMD transitions table:")
        for state in fsmd:
            print('  ' + state)
            for transition in fsmd[state]:
                print('    ' + 'nextstate: ' + transition['nextstate'] + ', condition: ' + transition[
                    'condition'] + ', instruction: ' + transition['instruction'])
        return fsmd
