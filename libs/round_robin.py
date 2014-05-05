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
	cur_pos = 0
	iterations = 0
	misses = 0
	while total_slice > 0:
		busy_count = 0
		use = [False for _ in range(len(task_list))]
		while busy_count <= num_processors:
			if use[cur_pos] == True:
				break
			elif _cpy_list[cur_pos] != 0:
				use[cur_pos]=True
				busy_count += 1
				total_slice -= 1
				_cpy_list[cur_pos] -= 1
			cur_pos += 1
			cur_pos %= len(task_list)
		iterations += 1
		for i in range(len(task_list)):
			lag = (task_list[i] * iterations / _cpy) - _cpy_list[i]
			if lag > 0:
				misses += math.floor(lag)
	return misses


if __name__ == '__main__':
	y = [0]*20
	x = [0]*20
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
	plt.plot(x, y)
	plt.show()
