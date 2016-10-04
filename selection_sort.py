import random
from datetime import datetime

def randomNumArrayGen(max, length):
	arr = []
	for count in range(length):
		arr.append(int(round(random.random()*max)))
	return arr

def selectionSort(arr):
	for i in range(0,len(arr)):
		lowest = arr[i]
		index = i
		for n in range(1+i, len(arr)):
			if arr[n] < lowest:
				#perform swap
				index = n
				lowest = arr[n]
		temp = arr[i]
		arr[i] = lowest
		arr[index] = temp
	arr[index] = temp
	return arr





now1 = datetime.now().microsecond
print selectionSort(randomNumArrayGen(500, 10))
now2 = datetime.now().microsecond
print(str(now2 - now1) + " microseconds")
