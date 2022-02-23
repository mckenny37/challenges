class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)]
              for i in range(len(text1) + 1)]

        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]

    def longestCommonSubsequenceRecursive(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0
        if text1[0] == text2[0]:
            return self.longestCommonSubsequence(text1[1:], text2[1:])+1
        else:
            return max(self.longestCommonSubsequence(text1, text2[1:]), self.longestCommonSubsequence(text1[1:], text2))


def main() -> None:
    text1: str = "abcba"
    text2: str = "abcbcba"
    solution: Solution = Solution()
    x = solution.longestCommonSubsequence(text1, text2)

    print(x)


if __name__ == "__main__":
    main()
