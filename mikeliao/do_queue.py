from multiprocessing import Process, Queue
import os, time, random

def write(q):
	print('pw pid: %s' % os.getpid())
	for i in ['A', 'B', 'C']:
		print('put %s into queue' % i)
		q.put(i)
		time.sleep(random.random())

def read(q):
	print('pr pid: %s' % os.getpid())
	while True:
		value = q.get()
		print('get %s from queue' % value)

if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))

	pw.start()
	pr.start()
	pw.join()
	pr.terminate()
