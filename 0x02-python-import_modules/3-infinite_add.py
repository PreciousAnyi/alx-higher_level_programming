#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	argc = len(sys.argv) - 1
	total_sum = 0
	for i in range(argc):
		total_sum += int(sys.argv[i + 1])
	print("{}".format(total_sum))

