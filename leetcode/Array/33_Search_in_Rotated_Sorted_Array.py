from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = 0
        b = len(nums)-1
        while(b-a > 1):
            pivot = (a+b)//2
            print(a)
            print(b)
            print(pivot)
            if nums[a] < nums[pivot]:
                if nums[a] <= target <= nums[pivot]:
                    b = pivot
                    print("b = pivot: " + str(b))
                else:
                    a = pivot+1
                    print("a = pivot + 1: " + str(a))
            else:
                if nums[a] <= target or target <= nums[pivot]:
                    b = pivot
                    print("b = pivot: " + str(b))
                else:
                    a = pivot+1
                    print("a = pivot + 1: " + str(a))

        if nums[a] == target:
            return a
        elif nums[b] == target:
            return b
        else:
            return -1


test = Solution()
nums = [5,1,3]
target = 3
ret = test.search(nums, target)
print(ret)
