# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # turns the array into a set, such that we can check whether
        # an element i has a left neighbor 
        # (if dne, i is the start of the sequence) and a right neighbor 
        # (if dne, i is the end of the sequence)
        numSet = set(nums)
        longest_sequence = 0 

        for i in numSet:
            # if there are no left neighbor, i is the start 
            if ((i-1) not in numSet):
                length = 0
                # increase length as we find consecutive elements
                while ((i + length) in numSet):
                    length = length + 1
                # set longest_sequence to be the maximum val so far
                longest_sequence = max(longest_sequence, length)
                
        return longest_sequence

