def find_max(array):
	if len(array) == 0:
		return None
	return binary_search(array, 0, len(array) - 1)
def binary_search(array, start, end):
	if end < start:
		return None
	middle = (start + end) / 2
	if middle == len(array) - 1 or array[middle] > array[middle+1]:
		return array[middle]
	if array[middle] < array[len(array) - 1]:
		return binary_search(array, start, middle-1)
	elif array[middle] > array[len(array) - 1]:
		return binary_search(array, middle+1, end)
	else:
		return array[middle]

def test():
	assert(find_max([7, 8,9,10,11,12,13,1,2,3]) == 13), "More than half shifted"
	assert(find_max([5, 6, 7, 1, 2, 3]) == 7), "General Test"
	assert(find_max([1]) == 1), "Single array"
	assert(find_max([11,2,3,4,5,6,7,8,9]) == 11), "All but one shifted"  
	assert(find_max([2,3,4,5,6,7,8,9, 1]) == 9), "Only one shifted"  
test()
