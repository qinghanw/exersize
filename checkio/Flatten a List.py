def flat_list(array):
	arr = []
	for i in array:
		if isinstance(i, int):
			arr.append(i)
		else:
			arr.extend(flat_list(i))
	return arr