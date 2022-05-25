class Solution:
    def numDecodings(self, s: str) -> int:
        ctr = 0
        dp = [1 for x in range(len(s) + 1)]
        dp[-1] = 1  # base case where there is one way to return value
        for i in reversed(range(len(s))):
            dp[i] = dp[i+1]  # default to value not changing
            if s[i] == '0':
                if i == 0:
                    return 0
                if not (s[i-1] == '1' or s[i-1] == '2'):
                    return 0
            if s[i] == '1' and i <= len(s)-2:
                if '3' <= s[i+1] <= '9':
                    dp[i] = dp[i+1] + dp[i+2]
                elif '1' <= s[i+1] <= '2':
                    if i <= len(s) - 3:
                        if s[i+2] != '0':
                            dp[i] = dp[i+1] + dp[i+2]
                    else:
                        dp[i] = dp[i+1] + dp[i+2]
            elif s[i] == '2' and i <= len(s)-2:
                if '3' <= s[i+1] <= '6':
                    dp[i] = dp[i+1] + dp[i+2]
                elif '1' <= s[i+1] <= '2':
                    if i <= len(s) - 3:
                        if s[i+2] != '0':
                            dp[i] = dp[i+1] + dp[i+2]
                    else:
                        dp[i] = dp[i+1] + dp[i+2]

        return dp[0]


def main() -> None:
    s = "1201234"
    solution = Solution()
    num = solution.numDecodings(s)

    print(num)


if __name__ == "__main__":
    main()
