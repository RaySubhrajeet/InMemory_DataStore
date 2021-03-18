from collections import deque
import copy

value_map = {}
count_map = {}
value_stack = []
count_stack = []
value_stack.append(value_map)
count_stack.append(count_map)
changed = False

while True :
	input1 = input()
	if not input1:
		exit()
	command = input1.split()

	if command[0] == "END":
		exit()
	
	elif command[0] == "SET":
		if command[1] in value_stack[-1].keys():
			temp = value_stack[-1][command[1]]
			value_stack[-1][command[1]] = command[2]
			count_stack[-1][temp] = count_stack[-1][temp] - 1
			if count_stack[-1][temp] == 0:
				del count_stack[-1][temp]         

		else:
			value_stack[-1][command[1]] = command[2]

		if command[2] in count_stack[-1].keys():
			count_stack[-1][command[2]] = count_stack[-1][command[2]] + 1
		
		else:
			count_stack[-1][command[2]] = 1
		if len(value_stack) > 1:
			changed = True
		# print(str(command[2]) + "\n")

	elif command[0] == "GET":
		if command[1] in value_stack[-1].keys():
			print(value_stack[-1][command[1]])
			
		else:
			print("NULL")

	elif command[0] == "UNSET":
		temp = value_stack[-1][command[1]]
		del value_stack[-1][command[1]]
		count_stack[-1][temp] = count_stack[-1][temp] - 1
		if len(value_stack) > 1:
			changed = True


	elif command[0] == "NUMEQUALTO":
		if command[1] in count_stack[-1].keys():
			print(count_stack[-1][command[1]])
			
		else:
			print("0")
	

	
	# Transactional commands
	
	elif command[0] == "BEGIN":
		value_copy = copy.deepcopy(value_stack[-1])
		count_copy = copy.deepcopy(count_stack[-1])
		count_stack.append(count_copy)
		value_stack.append(value_copy)

	elif command[0] == "ROLLBACK":
		if len(value_stack) > 1:
			value_stack.pop()
			count_stack.pop()
			if not changed:
				print("NO TRANSACTION\n")

			if len(value_stack) == 1:
				changed = False
		else:
			print("NO TRANSACTION")



	elif command[0] == "COMMIT":
		value_copy = copy.deepcopy(value_stack[-1])
		count_copy = copy.deepcopy(count_stack[-1])
		value_stack.clear()
		count_stack.clear()
		value_stack.append(value_copy)
		count_stack.append(count_copy)
		if not changed:
			print("NO TRANSACTION")
		changed = False



	else:
		continue


