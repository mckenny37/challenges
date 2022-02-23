from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        bits: List[int] = [0]
        base2: int = 1
        base2Count: int = 0
        
        for i in range(1,n+1):
            if base2Count == base2:
                base2 *= 2
                base2Count = 0
            bits.append(1 + bits[base2Count])
            print(bits[i])
            base2Count += 1

        return bits
    

def main() -> None:
    n: int = 10

    solution: Solution = Solution()

    out = solution.countBits(n)

    print(out)


if __name__ == "__main__":
    main()