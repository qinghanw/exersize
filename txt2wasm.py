import sys

def txt2wasm(bytecode, wasm):
	bytecode.strip('\n')
	bytecode.strip()
	length = int(len(bytecode) / 2)
	if length == 0:
		return
	list_nums = []

	for i in range(length):
		chs = bytecode[2*i:2*i+2]
		num = int(chs, 16)
		list_nums.append(num)

	#print(list_nums[:100])
	fb = open(wasm, "wb")
	fb.write(bytes(list_nums))
	fb.close()


def readFile(txt, wasm):
	file = open(txt, "r")
	count = 0
	try:
		while True:
			bytecode = file.readline()
			if bytecode:
				count += 1
				txt2wasm(bytecode, wasm)
			else:
				break
		print(count)
	finally:
		file.close()

if __name__ == '__main__':
	readFile(sys.argv[1], sys.argv[2])