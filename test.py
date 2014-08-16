#! /bin/python
#Test file for testing generate, round robin and pre-emptive scheduling techniques.
#Authors: Ranu Vikram, Vikram Bishnoi, Parag Gangil



import generator
import round_robin
import preemptive
import matplotlib.pyplot as plt
import random
import os
import copy

scale_const = 1000

if __name__ == '__main__':
	no_points = int(raw_input('Provide the number of points to be plotted: '))
	round_robin_x = [0] * no_points
	round_robin_y = [0] * no_points
	preemtvie_x = [0] * no_points
	preemtvie_y = [0] * no_points
	points_covered = 0
	perc = 0
	no_tasks = raw_input("Enter no. of tasks for obtaining the graph: ")
	print 'Misses vs. Processor'
	for i in range(1, 10000000, 1):
		proc_ct = i
		for fc in range(5):
			tasks = generator.get_random_data(proc_ct, int(no_tasks), scale_const)
			file_concerned = open('testcase.txt', 'r')
			proc_ct = int(file_concerned.readline())
			task_ct = int(file_concerned.readline())
			cpy_ = copy.deepcopy(tasks)
			round_robin_y[points_covered] += round_robin.schedule(tasks, proc_ct)
			tasks = copy.deepcopy(tasks)
			preemtvie_y[points_covered] += preemptive.schedule(tasks, proc_ct)
		round_robin_y[points_covered] /= 10.0
		preemtvie_y[points_covered] /= 10.0
		round_robin_x[points_covered] = proc_ct
		preemtvie_x[points_covered] = proc_ct
		points_covered += 1
		if points_covered > no_points-1:
			break
	plt.plot(round_robin_x, round_robin_y, preemtvie_x, preemtvie_y)
	plt.show()

	points_covered = 0
	print 'Misses vs. Tasks'
	no_procs = raw_input("Enter the number of processors required: ")
	for i in range(1, 1000000, 2):
		task_ct = i
		for fc in range(10):
			tasks = generator.get_random_data(int(no_procs), task_ct, scale_const)
			file2 = open('testcase.txt', 'r')
			proc_ct = int(file2.readline())
			task_ct = int(file2.readline())
			_cpy = copy.deepcopy(tasks)
			round_robin_y[points_covered] += round_robin.schedule(tasks, proc_ct)
			tasks = copy.deepcopy(_cpy)
			preemtvie_y[points_covered] += preemptive.schedule(tasks, proc_ct)
		round_robin_y[points_covered] /= 10.0
		preemtvie_y[points_covered] /= 10.0
		round_robin_x[points_covered] = task_ct
		preemtvie_x[points_covered] = task_ct
		points_covered += 1
		if points_covered > no_points - 1:
			break
	
	plt.plot(round_robin_x, round_robin_y, preemtvie_x, preemtvie_y)
	plt.show()
