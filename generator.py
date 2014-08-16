import random


def get_random_data(processor_count, task_count, _scale):
		file_to_open = open('testcase.txt', 'w')
		file_to_open.write(str(processor_count) + "\n")
		file_to_open.write(str(task_count) + "\n")
		task_duration = [random.randint(200, 500) for count in range(task_count)]
		for i in task_duration:
                       file_to_open.write(str(i) + "\n")
		file_to_open.close()
		return task_duration
