def time_converter(time):
	# replace this for solution
	h, m = time.split(':')
	hour = int(h)
	if hour >= 12:
		tail = "p.m."
		if hour > 12:
			hour = hour - 12
	else:
		tail = "a.m."
	coverd = str(hour)+":"+m+" "+tail
	return coverd


if __name__ == '__main__':
	kk = time_converter('09:35')
	print(kk)