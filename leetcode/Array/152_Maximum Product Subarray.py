from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m_product = nums[0]
        curr_product_left = 1
        cur_product_right = 1
        first = True
        for x in range(len(nums)):
                if curr_product_left == 0:
                    curr_product_left = 1
                    cur_product_right = 1
                    first = True
                curr_product_left *= nums[x]
                if curr_product_left > m_product: m_product=curr_product_left
                if not first:
                    cur_product_right *= nums[x]
                    if cur_product_right > m_product: m_product=cur_product_right
                
                if nums[x] < 0: first = False
                    
        return m_product 

    

solve = Solution([1,1])