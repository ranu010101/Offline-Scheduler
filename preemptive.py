import math
import matplotlib.pyplot as plt
from Queue import PriorityQueue


def schedule(tasks, num_processors):
	_cpy_list = [t for t in tasks]
	total_slice = 0
	for i in tasks:
		total_slice += i
	_cpy = total_slice
	pq = PriorityQueue()
	temp_out_list = [0]*len(tasks)
	for i in range(len(tasks)):
		pq.put((1.0 / tasks[i], i))
	iterations = 0
	misses = 0
	while pq.empty() == False:
		temp_out_c = 0
		for i in range(num_processors):
			if pq.empty() == True:
				break
			else:
				temp_out_list[temp_out_c] = pq.get()[1]
				temp_out_c += 1
		for i in range(temp_out_c):
			tasks[temp_out_list[i]] -= 1
			if tasks[temp_out_list[i]] != 0:
				pq.put(((_cpy_list[temp_out_list[i]] - tasks[temp_out_list[i]]) * _cpy / _cpy_list[temp_out_list[i]], temp_out_list[i]))
		iterations += 1
		#print iterations
		for i in range(len(tasks)):
			lag = 1.0 * _cpy_list[i] * iterations / _cpy - (_cpy_list[i] - tasks[i])
			if lag > 0:
				misses += math.floor(lag)
	return misses
	
