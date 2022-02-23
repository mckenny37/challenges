from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        minSeq = [nums[0]]  # Keeps track of minimum at each point in sequence
        for n in nums[1:]:
            if n > minSeq[len(minSeq)-1]:
                minSeq.append(n)
            else:
                for i in range(len(minSeq)):
                    if n <= minSeq[i]:
                        minSeq[i] = n
                        break

        return len(minSeq)


def main() -> None:
    nums = [4, 10, 4, 3, 8, 9]
    solution = Solution()
    x = solution.lengthOfLIS(nums)
    print(x)


if __name__ == "__main__":
    main()
