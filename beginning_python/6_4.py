class Store:
	def init(selfs, data):
		data['first'] = {}
		data['middle'] = {}
		data['last'] = {}

	def lookup(self, data, label, name):
		return data[label].get(name)

	def storage(self, data, full_name):
		names = full_name.split()
		if len(names) == 2:
			names.insert(1, '')

		labels = 'first', 'middle', 'last'
		for label, name in zip(labels, names):
			people = self.lookup(data, label, name)
			if people:
				people.append(full_name)
			else:
				data[label][name] = [full_name]

if __name__ == '__main__':
	MyNames = {}
	Store().init(MyNames)
	Store().storage(MyNames, 'wu qing han')
	Store().storage(MyNames, 'Magnus Lie Hetland')
	Store().storage(MyNames, 'Robin Hood')
	Store().storage(MyNames, 'Robin Locksley')
	string = Store().lookup(MyNames, 'middle', 'han')
	print(MyNames)