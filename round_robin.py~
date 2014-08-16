import math
import matplotlib.pyplot as plt
import copy

def schedule(tasks, num_processors):
	use = [False for _ in range(len(tasks))]
	_cpy_list = copy.deepcopy(tasks)
	total = 0
	for i in tasks:
		total += i
	_cpy = total
	cur_pos = 0
	iterations = 0
	misses = 0
	while total > 0:
		active_tasks = 0
		use = [False for _ in range(len(tasks))]
		while active_tasks < num_processors:
			if use[cur_pos] == True:
				break
			elif _cpy_list[cur_pos] != 0:
				use[cur_pos]=True
				active_tasks += 1
				total -= 1
				_cpy_list[cur_pos] -= 1
			cur_pos += 1
			cur_pos %= len(tasks)
		iterations += 1
		for i in range(len(tasks)):
			lag = (1.0 * (tasks[i] * iterations*num_processors) / (1.0*_cpy)) - 1.0*(tasks[i] - _cpy_list[i])
			if lag >  0:
				misses += math.floor(lag)
	return misses

