def customer():
	r = ''
	while True:
		n = yield r
		print('-----', n)
		if not n:
			return
		print('customer %s' % n)
		r = '200 ok'

def producer(c):
	c.send(None)
	n = 0
	while n < 5:
		n += 1
		print('producer %s' % n)
		r = c.send(n)
		print('custeromer return: %s' % r)

if __name__ == '__main__':
	c = customer()
	producer(c)