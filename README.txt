IN Memory Data Store:

Key Functionality :
SET key value – Set a data store entry with variable key and value. Neither the key nor
value will contain spaces.

GET key – Print out the value of the variable key, or NULL if that variable is not set.

UNSET key – Unset the variable key, making it just like that variable was never set.

NUMEQUALTO value – Print out the number of entries that are currently set to value. If
no entries equal that value, print 0.

END – Exit the program. Your program will always receive this as its last command.

Transactional Functionality:

BEGIN – Open a new transaction block. Transaction blocks can be nested; a BEGIN
can be issued inside of an existing block.

ROLLBACK – Undo all of the commands issued in the current transaction block, and
close the block. Print nothing if successful, or print NO TRANSACTION if no transaction
is in progress.

COMMIT – Close all open transaction blocks, permanently applying the changes made
in them. Print nothing if successful, or print NO TRANSACTION if no transaction is in
progress. Any data commands that run outside of a transaction block should commit
immediately

Language used:
python

Runtime Requirements:

I have used python 3.9.1.
Any version of python above 3.0 will work


Example 1:
INPUT OUTPUT
BEGIN
SET a 10
GET a 10
BEGIN
SET a 20
GET a 20
ROLLBACK
GET a 10
ROLLBACK
GET a NULL
END

Example 2:
INPUT OUTPUT
BEGIN
SET a 30
BEGIN
SET a 40
COMMIT
GET a 40
ROLLBACK NO TRANSACTION
END

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
For GET, NUMEQUALTO output is displayed in next line.  
FOR COMMIT, ROLLBACK if successful there is n output. Else NO "TRANSACTION" is displayed in next line 



