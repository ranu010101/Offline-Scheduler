

def simulate(task_list, num_processors):
	use = [False for _ in range(len(task_list))]
	total_slice = 0
	for i in task_list:
		total_slice += i
	_cpy = total_slice
	cur_pos = 0
	iterations = 0
	lag = 0
	while total_slice > 0:
		busy_count = 0
		use = [False for _ in range(len(task_list))]
		while busy_count < num_processors:
			if use[cur_pos] == True:
				break
			elif task_list[cur_pos] != 0:
				use[cur_pos]=True
				busy_count += 1
				total_slice -= 1
			cur_pos += 1
			cur_pos %= len(task_list)
		iterations += 1
		lag += (iterations * num_processors - (_cpy - total_slice))
	return lag


if __name__ == '__main__':
