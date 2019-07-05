class CountList:
	def __init__(self, *args):
		self.values = [x for x in args]
		self.count = {}.fromkeys(range(len(self.values)), 0)

	def __getitem__(self, key):
		self.count[key] += 1
		return self.values[key]

