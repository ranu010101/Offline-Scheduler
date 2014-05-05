import random

processor_max=30
task_max=50
max_time_slices=500
min_time_slices=200

_scale=10000

def scale(_req, _processors):
	slice_total = 0
	for i in _req:
		slice_total += i
	n_scale = _scale * _processors
	n = len(_req)
	for i in range(n):
		_req[i] = _req[i] * n_scale
		_req[i] /= slice_total
	return _req
	

def generate(processor_count, task_count):
		opfile = open('testcase.txt', 'w')
		opfile.write(str(processor_count) + "\n")
		opfile.write(str(task_count) + "\n")
		slice_req = [random.randint(min_time_slices, max_time_slices) for _ in range(task_count)]
		slice_req = scale(slice_req, processor_count)
		for i in slice_req:
			opfile.write(str(i) + "\n")
		opfile.close()
		

if __name__ == '__main__':
	generate(processor_max, task_max)
