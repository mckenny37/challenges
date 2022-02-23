from re import A
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[amount] if dp[amount] < amount+1 else -1


def main() -> None:
    coins: List[int] = [1, 2, 5]
    amount: int = 11
    solution: Solution = Solution()

    output = solution.coinChange(coins, amount)

    print(output)


if __name__ == "__main__":
    main()
