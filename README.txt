

Language used:
python

Runtime Requirements:

I have used python 3.9.1.
Any version of python above 3.0 will work


Command to Run:

python dataStore.py


Time Spent:
~2 hours

Approach:

I have used 2 maps(dictionary) and a 2 stack to implement this.
value_map : First maps stores the key- value pair.
count_map : The second map stores the count of each value stored for the NUMEQUALTO operation

The stacks are  used to implement different transaction. value_stack is stack of value_maps and count_stackis fr count_map

At first I create value_map and count_map and push to value_stack and count_stack

All operation are done on the stack top.

When a new transaction starts, I do a deepcopy of the stacktop and push it to the respective stacks and now any changes will be done to these new object.

When there is a ROLLBACK operation, pop from both the stacks.

When there is a COMMIT operation, store both the stacktops into a temporary variables and  clear the entire stack and repush the temporary objects into respective stacks.
 
Each operation happens in constant time O(1).
 

Command:

After each command press enter for successful execution
A irrelevant command will have no effect


OUTPUT Format:

For SET, UNSET, BEGIN there is no output
For GET, NUMEQUALTO output is displayed in next line.  (different from given requirement which needed output to be in same line)
FOR COMMIT, ROLLBACK if successful there is n output. Else NO "TRANSACTION" is displayed in next line 



