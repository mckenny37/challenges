from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def combinedOrDefault(x: List[int], y: List[int]) -> List[List[int]]:
            if x[1] < y[0]:
                return [x, y]
            return [[min(x[0],y[0]),max(x[1],y[1])]]

        intervalsSorted = sorted(intervals)
        result: List[List[int]] = []
        
        for interval in intervalsSorted:
            if len(result) == 0:
                result.append(interval)
            
            for newInterval in combinedOrDefault(result.pop(), interval):
                result.append(newInterval)

        return result

def main() -> None:
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    merge = Solution().merge(intervals)
    print(merge)
    
if __name__ == "__main__":
    main()