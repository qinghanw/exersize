import multiprocessing as mp
import time

def fun(block_range):
	print(mp.current_process().name, block_range)
	for i in block_range:
		print('-------------------')


if __name__ == '__main__':
	print('-----start')
	pool = mp.Pool(3)
	pool.map_async(fun, [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
	print('-----end')
	n = 0
	while True:
		n += 1
		print(n)
		time.sleep(0.5)
