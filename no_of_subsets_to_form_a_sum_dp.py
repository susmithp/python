"""
#********************************************************************************
#* Author : Susmith Poochali
#*
#* Program to find the number of subsets that adds up to a sum using Dynammic Programming
#*
#* Algorithm makes use of below logic:
#* Number of subsets that adds upto the sum using element at a particular index of list is
#* always equal to sum of number of subsets which includes the element at that particular index and 
#* number of subsets without element at that particular index.
#*
#*
#* arr = [2, 4, 6, 12]
#* Number of subsets using [12] = No of subsets which includes [12] + No of subsets which excludes [12]
#*
#*
#* Program needs two inputs
#* arr - List of integers
#* sum - Integer
#********************************************************************************
"""

# Inputs
list_of_ints = [2,4,6,10]
sum = 16
mem = {}


def find_sum_of_subsets(arr, sum, mem):
	"""
	Recursivly calls find_subsets method to find no of subset
	Sort the list, as we are going from right most element
	Algorithm requires list to be sorted in accending order
	
	Parameters:
	-----------
	arr 	: List
		List of integers to find the subsets
	total 	: Integer
		Sum of subsets will adds ups to this total
		
	Returns: 
	-------
	Integer
		Number of subsets
	"""
	
	arr.sort()
	# First find the no of subset with last element of list
	return find_subsets(arr, sum, len(arr) -1, mem)

def find_subsets(arr, total, index, mem):
	"""
	Recursion function to find no of subsets. It starts from 
	last index and ends when index is less than 0
	It total is 0, then we find a subset
	Intermittent results are saved in a dict to save improve the time complexity
	
	Parameters:
	-----------
	arr 	: List
		List of integers to find the subsets
	total 	: Integer
		Sum of subsets will adds ups to this total
	index 	: Integer
		Current Index of array
		
	Returns: 
	-------
	Integer
		Number of subsets	
	"""
	key = "{}:{}".format(total, index)
	if key in mem:
		return mem[key]
	if total == 0:
		# If total is 0, then a subset is found
		return 1
	elif total < 0:
		# if total is negative, no subset found for this sets
		return 0
	elif index < 0:
		# if index is negative and total is not zero, no subset found for this sets
		return 0
	if total < arr[index]:
		# if element at index is greater than total, we cannot form a set with that element
		# So skip that element, and proceed with rest
		mem[key] = find_subsets(arr, total, index-1, mem)
	# Total no of subsets using element at [index] is always equal to sum of subsets with 
	# element at [index] excluded  and sum of subsets with element included
	mem[key] = find_subsets(arr, total - arr[index], index-1, mem) + find_subsets(arr, total, index-1, mem)
	return mem[key]

# Execution begins here
if __name__ == '__main__':
	print('No of subset that adds up to {} is {}'.format(sum, find_sum_of_subsets(list_of_ints, sum, mem)))