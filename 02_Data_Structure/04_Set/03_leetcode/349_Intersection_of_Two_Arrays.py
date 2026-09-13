# Given two integer arrays, return their intersection. 
# Each element in the result must be unique.

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return list(set(nums1) & set(nums2))
        
