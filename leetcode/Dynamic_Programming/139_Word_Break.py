from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dpList = [0 for i in range(len(s) + 1)]
        dpList[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                if dpList[j]:
                    if s[j:i] in wordDict:
                        dpList[i] = True

        return dpList[len(s)]


def main() -> None:
    s = "catsanddog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    solution = Solution()
    x = solution.wordBreak(s, wordDict)

    print(x)


if __name__ == "__main__":
    main()
