"""
#********************************************************************************
#* Author : Susmith Poochali
#*
#* Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#* You may assume that each input would have exactly one solution, and you may not use the same element twice.
#*
#*  Time complexity : O(n)
#*
#*  Example:
#*
#* 		Given nums = [2, 7, 11, 15], target = 9,
#*
#*		Because nums[0] + nums[1] = 2 + 7 = 9,
#*		return [0, 1].
#*
#* Program needs two inputs
#* nums 	- List of integers
#* target 	- Integer
#********************************************************************************
"""
from typing import List

class Sum:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		"""
		Function iterate and inserts elements into the dictionary, 
		also check if current element's complement already exists in the dictionary. 
		If it exists, we have found a solution and return immediately.
		
		Parameters:
		-----------
		nums 	: List
			Given an array of integers
		target 	: Integer
			specific target
			
		Returns: 
		-------
		List
			List of Indexes
		"""
		dic_nums = {}
		for i in range(len(nums)):
			diff = target-nums[i]
			if diff in dic_nums:
				return [dic_nums[diff], i]
			dic_nums[nums[i]] = i
		return []
		
# Execution begins here
if __name__ == '__main__':
	target = 9
	nums = [2, 9, 11, 15, 7]
	sum = Sum().twoSum(nums, target)
	print('Index of two elements in array that adds up to target [{}] is {}'.format(target, sum))