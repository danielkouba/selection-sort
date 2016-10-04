import random
from datetime import datetime

def randomNumArrayGen(max, length):
	arr = []
	for count in range(length):
		arr.append(int(round(random.random()*max)))
	return arr

def selectionSort():
	unsorted = [5,4,3,6,2,1]
	tempIndex = 0
	for i in range(len(unsorted)):
		smallest = unsorted[i]
		for n in range(1,len(unsorted)):
			if unsorted[n] < smallest:
				smallest = unsorted[n]
				tempIndex = n
		print unsorted
		(unsorted[i], unsorted[tempIndex]) = (unsorted[tempIndex], unsorted[i])
	



selectionSort()



# var arr = [6,5,4,2,1];

# for (var i = 0; i < arr.length; i++){
#   var lowest = arr[i];
#   var index = i;
#   for (var n = 1+i; n < arr.length; n++){
#     if (arr[n] < lowest){
#       //perform swap
#       index = n;
#       lowest = arr[n];
#     }
#   }
#   var temp = arr[i];
#   arr[i] = lowest;
#   arr[index] = temp;
#   console.log(arr);
# }
# arr[index] = temp;
# console.log(arr)



# now1 = datetime.now().microsecond
# print selectionSort()
# now2 = datetime.now().microsecond
# print(str(now2 - now1) + " microseconds")
