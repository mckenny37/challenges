from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_a: int = 0
        l,r = 0, len(height)-1
        while l < r:
            min_h = min(height[l],height[r]) 
            area = min_h * (r-l)
            max_a = max(max_a,area)
            
            if min_h == height[l]:
                l += 1
            else:
                r -= 1
            
            
        return max_a    


def main() -> None:
    height: List[int] = [6,4,3,1,4,6,99,62,1,2,6]
    solution = Solution()
    max = solution.maxArea(height)

    print(max)

if __name__ == "__main__":
    main()