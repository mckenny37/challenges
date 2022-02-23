from __future__ import annotations
from typing import List, Dict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips: List[List[int]] = []

        nums.sort()
        for i in range(0, len(nums)):
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] < -nums[i]:
                    left += 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
                else:
                    trips.append([nums[i],nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                
        return trips

def main() -> None:
    solution = Solution()

    list = [-1,0,1,2,-1,4]

    trips = solution.threeSum(list)

    print(trips)

if __name__ == "__main__":
    main()



