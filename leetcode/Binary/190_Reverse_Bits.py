class Solution:
    def reverseBits(self, n: int) -> int:
        retVal = 0
        for i in range(32):
            shift = 31-i
            retVal |= ((n >> i) & 1) << shift
        return retVal


def main() -> None:
    n: int = 0b00000010100101000001111010011100
    solution: Solution = Solution()
    x = solution.reverseBits(n)
    print(x)
    print(format(x, 'b'))


if __name__ == "__main__":
    main()
