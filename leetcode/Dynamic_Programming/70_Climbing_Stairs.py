class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = {}
        stairs[1] = 1
        stairs[2] = 2
        for i in range(2, n):
            j = i+1
            stairs[j] = stairs[j-1] + stairs[j-2]

        return stairs[n]


def main() -> None:
    n: int = 6
    solution: Solution = Solution()
    x = solution.climbStairs(n)
    print(x)


if __name__ == "__main__":
    main()
