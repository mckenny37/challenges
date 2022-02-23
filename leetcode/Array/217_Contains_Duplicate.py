class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_map = {}
        for num in nums:
            if num in num_map:
                return True
            else:
                num_map[num] = True
        return False