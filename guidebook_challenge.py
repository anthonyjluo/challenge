def find_max(array):
	if len(array) == 0:
		return None
	return binary_search(array, 0, len(array) - 1)
def binary_search(array, start, end):
	while start <= end:
		middle = (start + end) / 2
		if middle == len(array) - 1 or array[middle] > array[middle+1]:
			return array[middle]
		if array[middle] < array[len(array) - 1]:
			end = middle - 1
		elif array[middle] > array[len(array) - 1]:
			start = middle + 1
		else:
			if array[start] == array[middle]:
				start += 1
			elif array[start] > array[middle]:
				end = middle - 1
			else:
				start = middle + 1
	return array[len(array) - 1]

def test():
	assert(find_max([7, 8,9,10,11,12,13,1,2,3]) == 13), "More than half shifted"
	assert(find_max([5, 6, 7, 1, 2, 3]) == 7), "General Test"
	assert(find_max([1]) == 1), "Single array"
	assert(find_max([11,2,3,4,5,6,7,8,9]) == 11), "All but one shifted"  
	assert(find_max([2,3,4,5,6,7,8,9, 1]) == 9), "Only one shifted"  
	assert(find_max([1,2,3,4,5,6,7,8,9]) == 9), "None shifted"  
	assert(find_max([5,5,7,8,9,9 ,2, 3, 4, 5]) == 9), "None shifted"  
	assert(find_max([5,5,5,6,5,5,5,5,5,5,5]) == 6), "All 5s but one 6 Case 1"
	assert(find_max([5,5,5,5,5,5,5,5,6,5,5]) == 6), "All 5s but one 6 Case 2"  
	assert(find_max([5,5,5,5,5,5,5,5,5,6,6]) == 6), "All 5s but one 6 Case 3"  
	assert(find_max([6,7,5,5,5,5,5,5,5,5,5,5]) ==7), "All 5s but one 6 Case 4"  
	assert(find_max([7, 8,9,10,11,11,11,1,2,3]) == 11), "General duplicates in array"  

