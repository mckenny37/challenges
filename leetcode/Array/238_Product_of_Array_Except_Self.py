class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products_left = [1]
        products_right = [1]
        for x in range(len(nums)-1):
            products_left.append(products_left[x]*nums[x])
            products_right.append(products_right[x]*nums[len(nums)-1-x])

        return [products_left[x]*products_right[len(nums)-1-x] for x in range(len(nums))]
