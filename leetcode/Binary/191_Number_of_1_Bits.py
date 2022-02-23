class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        #n & (n-1) removes the last 1 and all trailing 0s
        return 1 + self.hammingWeight(n & (n-1))

def main() -> None:
    solution = Solution()
    n: int = 11
    hw = solution.hammingWeight(n)

    print(hw)

if __name__ == "__main__":
    main()