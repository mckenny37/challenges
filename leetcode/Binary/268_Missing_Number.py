from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        retVal = 0
        # for i in range(len(nums)+1): +1 cause we need to go through missing number too
        for i in range(len(nums)):
            retVal ^= nums[i] ^ i

        # need to go through last number in range, index error if try to loop though len(nums)+1 in for loop
        return retVal ^ len(nums)


def main() -> None:
    nums = [0, 1, 2]
    solution = Solution()
    num = solution.missingNumber(nums)
    print(num)


if __name__ == "__main__":
    main()
