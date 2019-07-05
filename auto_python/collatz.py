def collatz(number):
	if number % 2 == 0:
		return number // 2
	else:
		return 3*number + 1

while True:
	try:
		num = int(input('enter a number:'))
	except ValueError as e:
		print('you must enter a number!')
	if 'num' in dir():
		break
while True:
	print(num)
	if num == 1:
		break
	num = collatz(num)

