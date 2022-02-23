from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]
        a = 0
        b = len(nums)-1
        while a < b:
            pivot = (a+b)//2
            if nums[a] < min: min = nums[a]
            if nums[a] <= nums[pivot]:
                a = pivot+1
            else:
                if nums[b] < min: min = nums[b]
                b = pivot
        if nums[a] < min: min = nums[a]
        return min
    
nums = [3,4,5,1,2]
test = Solution()   
a = test.findMin(nums) 
print(a)   



    