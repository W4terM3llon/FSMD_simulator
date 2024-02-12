


    #
    # Description:
    # This function executes a Python compatible operation passed as string
    # on the operands stored in the dictionary 'inputs'
    #
    def execute_setinput(self, operation):
        operation_clean = operation.replace(' ', '')
        operation_split = operation_clean.split('=')
        target = operation_split[0]
        expression = operation_split[1]
        self.inputs[target] = eval(expression, {'__builtins__': None}, self.inputs)
        return


    #
    # Description:
    # This function executes a Python compatible operation passed as string
    # on the operands stored in the dictionaries 'variables' and 'inputs'
    #
    def execute_operation(self, operation):
        operation_clean = operation.replace(' ', '')
        operation_split = operation_clean.split('=')
        target = operation_split[0]
        expression = operation_split[1]
        self.variables[target] = eval(expression, {'__builtins__': None}, self.merge_dicts(self.variables, self.inputs))
        return


    #
    # Description:
    # This function executes a list of operations passed as string and spaced by
    # a single space using the expression defined in the dictionary 'operations'
    #
    def execute_instruction(self, instruction):
        if instruction == 'NOP' or instruction == 'nop':
            return
        instruction_split = instruction.split(' ')
        for operation in instruction_split:
            self.execute_operation(self.operations[operation])
        return


    #
    # Description:
    # This function evaluates a Python compatible boolean expressions of
    # conditions passed as string using the conditions defined in the variable 'conditions'
    # and using the operands stored in the dictionaries 'variables' and 'inputs
    # It returns True or False
    #
    def evaluate_condition(self, condition):
        if condition == 'True' or condition=='true' or condition == 1:
            return True
        if condition == 'False' or condition=='false' or condition == 0:
            return False
        condition_explicit = condition
        for element in self.conditions:
            condition_explicit = condition_explicit.replace(element, self.conditions[element])
        #print('----' + condition_explicit)
        return eval(condition_explicit, {'__builtins__': None}, self.merge_dicts(self.variables, self.inputs))


    #
    # Description:
    # Support function to merge two dictionaries.
    #
    def merge_dicts(self, *dict_args):
        result = {}
        for dictionary in dict_args:
            result.update(dictionary)
        return result


fsmdInstance = FsmdSim()


print(fsmdInstance.__dict__.keys())

#######################################
# Start to simulate
cycle = 0
state = fsmdInstance.initial_state

print('\n---Start simulation---')
print('At the beginning of the simulation the status is:')
print('Variables:')
for (k, v) in fsmdInstance.variables:
    print(f'{k} = {v}')
print(F'Initial state: {fsmdInstance.initial_state}')
print('--------------------------------------------------')

######################################
######################################
# Write your code here!
######################################
######################################

print('\n---End of simulation---')

#
# Description:
# This is a code snippet used to update the inputs values according to the
# stimuli file content. You can see here how the 'fsmd_stim' variable is used.
#
try:
    if (not(fsmd_stim['fsmdstimulus']['setinput'] is None)):
        for setinput in fsmd_stim['fsmdstimulus']['setinput']:
            if type(setinput) is str:
                #Only one element
                if int(fsmd_stim['fsmdstimulus']['setinput']['cycle']) == cycle:
                    execute_setinput(fsmd_stim['fsmdstimulus']['setinput']['expression'])
                break
            else:
                #More than 1 element
                if int(setinput['cycle']) == cycle:
                    execute_setinput(setinput['expression'])
except:
    pass

#
# Description:
# This is a code snipppet used to check the endstate value according to the
# stimuli file content. You can see here how the 'fsmd_stim' variable is used.
#
try:
    if (not(fsmd_stim['fsmdstimulus']['endstate'] is None)):
        if state == fsmd_stim['fsmdstimulus']['endstate']:
            print('End-state reached.')
            repeat = False
except:
    pass
