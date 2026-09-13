# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.

#You must write an algorithm that runs in O(n) time.


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for n in num_set:

            if n - 1 not in num_set:
                count = 1
                current = n

                while current + 1 in num_set:
                    current += 1
                    count += 1

                max_len = max(max_len, count)

        return max_len