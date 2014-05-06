import generator
import math
import matplotlib.pyplot as plt
from Queue import PriorityQueue


def simulate(task_list, num_processors):
	_cpy_list = [t for t in task_list]
	total_slice = 0
	for i in task_list:
		total_slice += i
	_cpy = total_slice
	pq = PriorityQueue()
	temp_out_list = [0]*len(task_list)
	for i in range(len(task_list)):
		pq.put((1.0 / task_list[i], i))
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
			task_list[temp_out_list[i]] -= 1
			if task_list[temp_out_list[i]] != 0:
				pq.put(((_cpy_list[temp_out_list[i]] - task_list[temp_out_list[i]]) * _cpy / _cpy_list[temp_out_list[i]], temp_out_list[i]))
		iterations += 1
		#print iterations
		for i in range(len(task_list)):
			lag = _cpy_list[i] * iterations / _cpy - (_cpy_list[i] - task_list[i])
			if lag > 0:
				misses += math.floor(lag)
	return misses
	
if __name__ == '__main__':
	y = [0] * 20
	x = [0] * 20
	for i in range(1, 20):
		for fc in range(20):
			generator.generate(i, 20, 1000)
			f = open('testcase.txt', 'r')
			proc_count = int(f.readline())
			task_count = int(f.readline())
			tasks = [0] * task_count
			for j in range(task_count):
				tasks[j] = int(f.readline())
			y[i]+=simulate(tasks, proc_count)
		x[i]=i
		y[i] /= 20
		print x[i], y[i]
	plt.plot(x, y)
	plt.show()
