import generator
import math
import matplotlib.pyplot as plt

def simulate(task_list, num_processors):
	use = [False for _ in range(len(task_list))]
	_cpy_list = [t for t in task_list]
	total_slice = 0
	for i in task_list:
		total_slice += i
	_cpy = total_slice

