
# FSMD
This is FSMD project implemented in Python.
It includes 3 test cases, the third one was created by us. Run ```.\fsmd-sim.py``` file to use the project. 

In order to see ```in_extra_combinations``` from the stimuli file in action, remember to go to ```.\fsmdSim\test_3\stair_stim.xml``` and uncomment part of the code responsible for it.

You can use ```.\testCases\test_3\ClimbingStairs.py``` to compare the result from FSMD.

## Authors (Group 25)

- Adrian Maciejewski
- Elias Haynie-Gay
- Balint Regoczi


## Running test cases

To run the 1st test case run the following from the root of the project:

```bash
  python .\fsmd-sim.py 100 .\testCases\test_1\test_desc.xml

```
The output should be:
```
Welcome to the FSMD simulator! - Version ?? - Designed by ??

--FSMD description--
States:
  INITIALIZE
  COMPUTE
  DONE
Initial state:
  INITIALIZE
Inputs:
Variables:
  var_A
  var_TH
Operations:
  init_A : var_A = 10
  init_TH : var_TH = 0
  decr_A : var_A = var_A - 1
  incr_A : var_A = var_A + 1
Conditions:
  A_equal_TH : var_A == var_TH
  A_greater_TH : var_A > var_TH
  TH_greater_A : var_A < var_TH
FSMD transitions table:
  INITIALIZE
    nextstate: COMPUTE, condition: True, instruction: init_A init_TH
  COMPUTE
    nextstate: DONE, condition: A_equal_TH, instruction: NOP
    nextstate: COMPUTE, condition: A_greater_TH, instruction: decr_A
    nextstate: COMPUTE, condition: TH_greater_A, instruction: incr_A
  DONE
    nextstate: DONE, condition: True, instruction: NOP

---Start simulation---
At the beginning of the simulation the status is:
Variables:
  var_A = 0
  var_TH = 0
Initial state: INITIALIZE
--------------------------------------------------
Cycle: 0
Current state: INITIALIZE
Inputs:
The condition (True) is true.
Executing instruction: init_A init_TH
Next state: COMPUTE
At the end of cycle 0 execution, the status is:
Variables:
  var_A = 10
  var_TH = 0
--------------------------------------------------
Cycle: 1
Current state: COMPUTE
Inputs:
The condition (A_greater_TH) is true.
Executing instruction: decr_A
Next state: COMPUTE
At the end of cycle 1 execution, the status is:
Variables:
  var_A = 9
  var_TH = 0
--------------------------------------------------
Cycle: 2
Current state: COMPUTE
Inputs:
The condition (A_greater_TH) is true.
Executing instruction: decr_A
Next state: COMPUTE
At the end of cycle 2 execution, the status is:
Variables:
  var_A = 8
  var_TH = 0
--------------------------------------------------
Cycle: 3
Current state: COMPUTE
Inputs:
The condition (A_greater_TH) is true.
Executing instruction: decr_A
Next state: COMPUTE
At the end of cycle 3 execution, the status is:
Variables:
  var_A = 7
  var_TH = 0
--------------------------------------------------
Cycle: 4
Current state: COMPUTE
Inputs:
The condition (A_greater_TH) is true.
Executing instruction: decr_A
Next state: COMPUTE
At the end of cycle 4 execution, the status is:
Variables:
  var_A = 6
  var_TH = 0
--------------------------------------------------
Cycle: 5
Current state: COMPUTE
Inputs:
The condition (A_greater_TH) is true.
Executing instruction: decr_A
Next state: COMPUTE
At the end of cycle 5 execution, the status is:
Variables:
  var_A = 5
  var_TH = 0
--------------------------------------------------
Cycle: 6
Current state: COMPUTE
Inputs:
The condition (A_greater_TH) is true.
Executing instruction: decr_A
Next state: COMPUTE
At the end of cycle 6 execution, the status is:
Variables:
  var_A = 4
  var_TH = 0
--------------------------------------------------
Cycle: 7
Current state: COMPUTE
Inputs:
The condition (A_greater_TH) is true.
Executing instruction: decr_A
Next state: COMPUTE
At the end of cycle 7 execution, the status is:
Variables:
  var_A = 3
  var_TH = 0
--------------------------------------------------
Cycle: 8
Current state: COMPUTE
Inputs:
The condition (A_greater_TH) is true.
Executing instruction: decr_A
Next state: COMPUTE
At the end of cycle 8 execution, the status is:
Variables:
  var_A = 2
  var_TH = 0
--------------------------------------------------
Cycle: 9
Current state: COMPUTE
Inputs:
The condition (A_greater_TH) is true.
Executing instruction: decr_A
Next state: COMPUTE
At the end of cycle 9 execution, the status is:
Variables:
  var_A = 1
  var_TH = 0
--------------------------------------------------
Cycle: 10
Current state: COMPUTE
Inputs:
The condition (A_greater_TH) is true.
Executing instruction: decr_A
Next state: COMPUTE
At the end of cycle 10 execution, the status is:
Variables:
  var_A = 0
  var_TH = 0
--------------------------------------------------
Cycle: 11
Current state: COMPUTE
Inputs:
The condition (A_equal_TH) is true.
Executing instruction: NOP
Next state: DONE
At the end of cycle 11 execution, the status is:
Variables:
  var_A = 0
  var_TH = 0
--------------------------------------------------
Cycle: 12
Current state: DONE
Inputs:
The condition (True) is true.
Executing instruction: NOP
Next state: DONE
At the end of cycle 12 execution, the status is:
Variables:
  var_A = 0
  var_TH = 0
--------------------------------------------------
End-state reached.
End of simulation. Goodbye!

```

To run the 2nd test case run the following from the root of the project:

```bash
  python .\fsmd-sim.py 100 .\testCases\test_2\gcd_desc.xml  .\testCases\test_2\gcd_stim.xml

```
The output should be:
```
Welcome to the FSMD simulator! - Version ?? - Designed by ??

--FSMD description--
States:
  INITIALIZE
  TEST
  AMINB
  BMINA
  FINISH
Initial state:
  INITIALIZE
Inputs:
  in_A
  in_B
Variables:
  var_A
  var_B
Operations:
  init_A : var_A = in_A
  init_B : var_B = in_B
  A_minus_B : var_A = var_A - var_B
  B_minus_A : var_B = var_B - var_A
Conditions:
  A_equal_B : var_A == var_B
  A_greater_B : var_A > var_B
  B_greater_A : var_A < var_B
FSMD transitions table:
  INITIALIZE
    nextstate: TEST, condition: True, instruction: init_A init_B
  TEST
    nextstate: FINISH, condition: A_equal_B, instruction: NOP
    nextstate: AMINB, condition: A_greater_B, instruction: NOP
    nextstate: BMINA, condition: B_greater_A, instruction: NOP
  AMINB
    nextstate: TEST, condition: True, instruction: A_minus_B
  BMINA
    nextstate: TEST, condition: True, instruction: B_minus_A
  FINISH
    nextstate: FINISH, condition: True, instruction: NOP

---Start simulation---
At the beginning of the simulation the status is:
Variables:
  var_A = 0
  var_B = 0
Initial state: INITIALIZE
--------------------------------------------------
Cycle: 0
Current state: INITIALIZE
Inputs:
  in_A = 100
  in_B = 12
The condition (True) is true.
Executing instruction: init_A init_B
Next state: TEST
At the end of cycle 0 execution, the status is:
Variables:
  var_A = 100
  var_B = 12
--------------------------------------------------
Cycle: 1
Current state: TEST
Inputs:
  in_A = 0
  in_B = 0
The condition (A_greater_B) is true.
Executing instruction: NOP
Next state: AMINB
At the end of cycle 1 execution, the status is:
Variables:
  var_A = 100
  var_B = 12
--------------------------------------------------
Cycle: 2
Current state: AMINB
Inputs:
  in_A = 0
  in_B = 0
The condition (True) is true.
Executing instruction: A_minus_B
Next state: TEST
At the end of cycle 2 execution, the status is:
Variables:
  var_A = 88
  var_B = 12
--------------------------------------------------
Cycle: 3
Current state: TEST
Inputs:
  in_A = 0
  in_B = 0
The condition (A_greater_B) is true.
Executing instruction: NOP
Next state: AMINB
At the end of cycle 3 execution, the status is:
Variables:
  var_A = 88
  var_B = 12
--------------------------------------------------
Cycle: 4
Current state: AMINB
Inputs:
  in_A = 0
  in_B = 0
The condition (True) is true.
Executing instruction: A_minus_B
Next state: TEST
At the end of cycle 4 execution, the status is:
Variables:
  var_A = 76
  var_B = 12
--------------------------------------------------
Cycle: 5
Current state: TEST
Inputs:
  in_A = 0
  in_B = 0
The condition (A_greater_B) is true.
Executing instruction: NOP
Next state: AMINB
At the end of cycle 5 execution, the status is:
Variables:
  var_A = 76
  var_B = 12
--------------------------------------------------
Cycle: 6
Current state: AMINB
Inputs:
  in_A = 0
  in_B = 0
The condition (True) is true.
Executing instruction: A_minus_B
Next state: TEST
At the end of cycle 6 execution, the status is:
Variables:
  var_A = 64
  var_B = 12
--------------------------------------------------
Cycle: 7
Current state: TEST
Inputs:
  in_A = 0
  in_B = 0
The condition (A_greater_B) is true.
Executing instruction: NOP
Next state: AMINB
At the end of cycle 7 execution, the status is:
Variables:
  var_A = 64
  var_B = 12
--------------------------------------------------
Cycle: 8
Current state: AMINB
Inputs:
  in_A = 0
  in_B = 0
The condition (True) is true.
Executing instruction: A_minus_B
Next state: TEST
At the end of cycle 8 execution, the status is:
Variables:
  var_A = 52
  var_B = 12
--------------------------------------------------
Cycle: 9
Current state: TEST
Inputs:
  in_A = 0
  in_B = 0
The condition (A_greater_B) is true.
Executing instruction: NOP
Next state: AMINB
At the end of cycle 9 execution, the status is:
Variables:
  var_A = 52
  var_B = 12
--------------------------------------------------
Cycle: 10
Current state: AMINB
Inputs:
  in_A = 0
  in_B = 0
The condition (True) is true.
Executing instruction: A_minus_B
Next state: TEST
At the end of cycle 10 execution, the status is:
Variables:
  var_A = 40
  var_B = 12
--------------------------------------------------
Cycle: 11
Current state: TEST
Inputs:
  in_A = 0
  in_B = 0
The condition (A_greater_B) is true.
Executing instruction: NOP
Next state: AMINB
At the end of cycle 11 execution, the status is:
Variables:
  var_A = 40
  var_B = 12
--------------------------------------------------
Cycle: 12
Current state: AMINB
Inputs:
  in_A = 0
  in_B = 0
The condition (True) is true.
Executing instruction: A_minus_B
Next state: TEST
At the end of cycle 12 execution, the status is:
Variables:
  var_A = 28
  var_B = 12
--------------------------------------------------
Cycle: 13
Current state: TEST
Inputs:
  in_A = 0
  in_B = 0
The condition (A_greater_B) is true.
Executing instruction: NOP
Next state: AMINB
At the end of cycle 13 execution, the status is:
Variables:
  var_A = 28
  var_B = 12
--------------------------------------------------
Cycle: 14
Current state: AMINB
Inputs:
  in_A = 0
  in_B = 0
The condition (True) is true.
Executing instruction: A_minus_B
Next state: TEST
At the end of cycle 14 execution, the status is:
Variables:
  var_A = 16
  var_B = 12
--------------------------------------------------
Cycle: 15
Current state: TEST
Inputs:
  in_A = 0
  in_B = 0
The condition (A_greater_B) is true.
Executing instruction: NOP
Next state: AMINB
At the end of cycle 15 execution, the status is:
Variables:
  var_A = 16
  var_B = 12
--------------------------------------------------
Cycle: 16
Current state: AMINB
Inputs:
  in_A = 0
  in_B = 0
The condition (True) is true.
Executing instruction: A_minus_B
Next state: TEST
At the end of cycle 16 execution, the status is:
Variables:
  var_A = 4
  var_B = 12
--------------------------------------------------
Cycle: 17
Current state: TEST
Inputs:
  in_A = 0
  in_B = 0
The condition (B_greater_A) is true.
Executing instruction: NOP
Next state: BMINA
At the end of cycle 17 execution, the status is:
Variables:
  var_A = 4
  var_B = 12
--------------------------------------------------
Cycle: 18
Current state: BMINA
Inputs:
  in_A = 0
  in_B = 0
The condition (True) is true.
Executing instruction: B_minus_A
Next state: TEST
At the end of cycle 18 execution, the status is:
Variables:
  var_A = 4
  var_B = 8
--------------------------------------------------
Cycle: 19
Current state: TEST
Inputs:
  in_A = 0
  in_B = 0
The condition (B_greater_A) is true.
Executing instruction: NOP
Next state: BMINA
At the end of cycle 19 execution, the status is:
Variables:
  var_A = 4
  var_B = 8
--------------------------------------------------
Cycle: 20
Current state: BMINA
Inputs:
  in_A = 0
  in_B = 0
The condition (True) is true.
Executing instruction: B_minus_A
Next state: TEST
At the end of cycle 20 execution, the status is:
Variables:
  var_A = 4
  var_B = 4
--------------------------------------------------
Cycle: 21
Current state: TEST
Inputs:
  in_A = 0
  in_B = 0
The condition (A_equal_B) is true.
Executing instruction: NOP
Next state: FINISH
At the end of cycle 21 execution, the status is:
Variables:
  var_A = 4
  var_B = 4
--------------------------------------------------
Cycle: 22
Current state: FINISH
Inputs:
  in_A = 0
  in_B = 0
The condition (True) is true.
Executing instruction: NOP
Next state: FINISH
At the end of cycle 22 execution, the status is:
Variables:
  var_A = 4
  var_B = 4
--------------------------------------------------
End-state reached.
End of simulation. Goodbye!

```

To run the 3rd test case run the following from the root of the project:

```bash
  python .\fsmd-sim.py 100 .\testCases\test_3\stair_desc.xml .\testCases\test_3\stair_stim.xml
```
The output should be:
```
Welcome to the FSMD simulator! - Version ?? - Designed by ??

--FSMD description--
States:
  INITIALIZE
  TEST_INITIAL
  LOOP
  FINISH
Initial state:
  INITIALIZE
Inputs:
  in_max_step
  in_extra_combinations
Variables:
  var_current_step
  var_max_step
  var_previous_combinations
  var_final_combinations
  var_temp
Operations:
  init_max_steps : var_max_step = in_max_step
  add_extra_combinations : var_final_combinations = var_final_combinations + in_extra_combinations
  init_cur_step : var_current_step = 0
  init_prev : var_previous_combinations = 1
  init_final : var_final_combinations = 0
  set_var_final_step_to_1 : var_final_combinations = 1
  set_var_final_step_to_2 : var_final_combinations = 2
  incr_current_step : var_current_step = var_current_step + 1
  calculate_set_previous_step_values_step_1 : var_temp = var_previous_combinations + var_final_combinations
  calculate_set_previous_step_values_step_2 : var_previous_combinations = var_final_combinations
  calculate_set_previous_step_values_step_3 : var_final_combinations = var_temp
Conditions:
  var_max_step_less_than_or_equal_0 : var_max_step <= 0
  var_current_step_equals_0_and_max_at_least_1 : var_current_step == 0 and var_max_step >= 1
  var_current_step_equals_1_and_max_at_least_2 : var_current_step == 1 and var_max_step >= 2
  var_current_step_more_than_1_and_var_max_step_greater_than_2 : var_current_step > 1 and var_max_step > 2
  current_step_equals_max_step : var_current_step == var_max_step or var_current_step > var_max_step
  current_step_smaller_than_max_step : var_current_step < var_max_step
FSMD transitions table:
  INITIALIZE
    nextstate: TEST_INITIAL, condition: True, instruction: init_cur_step init_max_steps init_final add_extra_combinations
  TEST_INITIAL
    nextstate: FINISH, condition: var_max_step_less_than_or_equal_0, instruction: add_extra_combinations
    nextstate: TEST_INITIAL, condition: var_current_step_equals_0_and_max_at_least_1, instruction: set_var_final_step_to_1 add_extra_combinations incr_current_step init_prev
    nextstate: TEST_INITIAL, condition: var_current_step_equals_1_and_max_at_least_2, instruction: add_extra_combinations incr_current_step calculate_set_previous_step_values_step_1 calculate_set_previous_step_values_step_2 calculate_set_previous_step_values_step_3
    nextstate: LOOP, condition: var_current_step_more_than_1_and_var_max_step_greater_than_2, instruction: add_extra_combinations
  LOOP
    nextstate: FINISH, condition: current_step_equals_max_step, instruction: add_extra_combinations
    nextstate: LOOP, condition: current_step_smaller_than_max_step, instruction: add_extra_combinations calculate_set_previous_step_values_step_1 calculate_set_previous_step_values_step_2 calculate_set_previous_step_values_step_3 incr_current_step
  FINISH
    nextstate: FINISH, condition: True, instruction: NOP

---Start simulation---
At the beginning of the simulation the status is:
Variables:
  var_current_step = 0
  var_max_step = 0
  var_previous_combinations = 0
  var_final_combinations = 0
  var_temp = 0
Initial state: INITIALIZE
--------------------------------------------------
Cycle: 0
Current state: INITIALIZE
Inputs:
  in_max_step = 9
  in_extra_combinations = 0
The condition (True) is true.
Executing instruction: init_cur_step init_max_steps init_final add_extra_combinations
Next state: TEST_INITIAL
At the end of cycle 0 execution, the status is:
Variables:
  var_current_step = 0
  var_max_step = 9
  var_previous_combinations = 0
  var_final_combinations = 0
  var_temp = 0
--------------------------------------------------
Cycle: 1
Current state: TEST_INITIAL
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (var_current_step_equals_0_and_max_at_least_1) is true.
Executing instruction: set_var_final_step_to_1 add_extra_combinations incr_current_step init_prev
Next state: TEST_INITIAL
At the end of cycle 1 execution, the status is:
Variables:
  var_current_step = 1
  var_max_step = 9
  var_previous_combinations = 1
  var_final_combinations = 1
  var_temp = 0
--------------------------------------------------
Cycle: 2
Current state: TEST_INITIAL
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (var_current_step_equals_1_and_max_at_least_2) is true.
Executing instruction: add_extra_combinations incr_current_step calculate_set_previous_step_values_step_1 calculate_set_previous_step_values_step_2 calculate_set_previous_step_values_step_3
Next state: TEST_INITIAL
At the end of cycle 2 execution, the status is:
Variables:
  var_current_step = 2
  var_max_step = 9
  var_previous_combinations = 1
  var_final_combinations = 2
  var_temp = 2
--------------------------------------------------
Cycle: 3
Current state: TEST_INITIAL
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (var_current_step_more_than_1_and_var_max_step_greater_than_2) is true.
Executing instruction: add_extra_combinations
Next state: LOOP
At the end of cycle 3 execution, the status is:
Variables:
  var_current_step = 2
  var_max_step = 9
  var_previous_combinations = 1
  var_final_combinations = 2
  var_temp = 2
--------------------------------------------------
Cycle: 4
Current state: LOOP
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (current_step_smaller_than_max_step) is true.
Executing instruction: add_extra_combinations calculate_set_previous_step_values_step_1 calculate_set_previous_step_values_step_2 calculate_set_previous_step_values_step_3 incr_current_step
Next state: LOOP
At the end of cycle 4 execution, the status is:
Variables:
  var_current_step = 3
  var_max_step = 9
  var_previous_combinations = 2
  var_final_combinations = 3
  var_temp = 3
--------------------------------------------------
Cycle: 5
Current state: LOOP
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (current_step_smaller_than_max_step) is true.
Executing instruction: add_extra_combinations calculate_set_previous_step_values_step_1 calculate_set_previous_step_values_step_2 calculate_set_previous_step_values_step_3 incr_current_step
Next state: LOOP
At the end of cycle 5 execution, the status is:
Variables:
  var_current_step = 4
  var_max_step = 9
  var_previous_combinations = 3
  var_final_combinations = 5
  var_temp = 5
--------------------------------------------------
Cycle: 6
Current state: LOOP
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (current_step_smaller_than_max_step) is true.
Executing instruction: add_extra_combinations calculate_set_previous_step_values_step_1 calculate_set_previous_step_values_step_2 calculate_set_previous_step_values_step_3 incr_current_step
Next state: LOOP
At the end of cycle 6 execution, the status is:
Variables:
  var_current_step = 5
  var_max_step = 9
  var_previous_combinations = 5
  var_final_combinations = 8
  var_temp = 8
--------------------------------------------------
Cycle: 7
Current state: LOOP
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (current_step_smaller_than_max_step) is true.
Executing instruction: add_extra_combinations calculate_set_previous_step_values_step_1 calculate_set_previous_step_values_step_2 calculate_set_previous_step_values_step_3 incr_current_step
Next state: LOOP
At the end of cycle 7 execution, the status is:
Variables:
  var_current_step = 6
  var_max_step = 9
  var_previous_combinations = 8
  var_final_combinations = 13
  var_temp = 13
--------------------------------------------------
Cycle: 8
Current state: LOOP
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (current_step_smaller_than_max_step) is true.
Executing instruction: add_extra_combinations calculate_set_previous_step_values_step_1 calculate_set_previous_step_values_step_2 calculate_set_previous_step_values_step_3 incr_current_step
Next state: LOOP
At the end of cycle 8 execution, the status is:
Variables:
  var_current_step = 7
  var_max_step = 9
  var_previous_combinations = 13
  var_final_combinations = 21
  var_temp = 21
--------------------------------------------------
Cycle: 9
Current state: LOOP
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (current_step_smaller_than_max_step) is true.
Executing instruction: add_extra_combinations calculate_set_previous_step_values_step_1 calculate_set_previous_step_values_step_2 calculate_set_previous_step_values_step_3 incr_current_step
Next state: LOOP
At the end of cycle 9 execution, the status is:
Variables:
  var_current_step = 8
  var_max_step = 9
  var_previous_combinations = 21
  var_final_combinations = 34
  var_temp = 34
--------------------------------------------------
Cycle: 10
Current state: LOOP
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (current_step_smaller_than_max_step) is true.
Executing instruction: add_extra_combinations calculate_set_previous_step_values_step_1 calculate_set_previous_step_values_step_2 calculate_set_previous_step_values_step_3 incr_current_step
Next state: LOOP
At the end of cycle 10 execution, the status is:
Variables:
  var_current_step = 9
  var_max_step = 9
  var_previous_combinations = 34
  var_final_combinations = 55
  var_temp = 55
--------------------------------------------------
Cycle: 11
Current state: LOOP
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (current_step_equals_max_step) is true.
Executing instruction: add_extra_combinations
Next state: FINISH
At the end of cycle 11 execution, the status is:
Variables:
  var_current_step = 9
--------------------------------------------------
Cycle: 12
Current state: FINISH
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (True) is true.
Executing instruction: NOP
Next state: FINISH
At the end of cycle 12 execution, the status is:
Variables:
  var_current_step = 9
  var_max_step = 9
  var_previous_combinations = 34
  var_final_combinations = 55
  var_temp = 55
--------------------------------------------------
Cycle: 13
Current state: FINISH
Inputs:
  in_max_step = 0
  in_extra_combinations = 0
The condition (True) is true.
Executing instruction: NOP
Next state: FINISH
At the end of cycle 13 execution, the status is:
Variables:
  var_current_step = 9
  var_max_step = 9
  var_previous_combinations = 34
  var_final_combinations = 55
  var_temp = 55
--------------------------------------------------
End-state reached.
End of simulation. Goodbye!

```
