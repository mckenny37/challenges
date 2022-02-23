from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_sum = nums[0]
        curr_sum = 0
        for x in range(len(nums)):
                if curr_sum < 0:
                    curr_sum = 0
                curr_sum += nums[x]
                if curr_sum > m_sum: m_sum=curr_sum
        return m_sum


    def __init__(self, nums: List[int]):
        val = self.maxSubArray(nums) 

    

solve = Solution([1,1])

