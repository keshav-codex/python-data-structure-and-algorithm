# Given an integer array nums, return True if any value appears at least twice, 
# and return False if every element is distinct.


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        
        return True if len(nums) != len(num_set) else False
        
