from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def noOverlap(x, y):
            return (x[0] <= x[1] < y[0] <= y[1]) or (y[0] <= y[1] < x[0] <= x[1]) 

        def combine(interval, nextInterval):
            x = min(interval[0], nextInterval[0])
            y = max(interval[1], nextInterval[1])
            return [x,y]

        result: List[List[int]] = []
        notAdded = True

        if len(intervals) < 1:
            result.append(newInterval)
            return result
           
        result.append(intervals[0])
        
        for i in range(len(intervals)):
            prev = result[-1]
            curr = intervals[i]
            if (noOverlap(prev, curr)):
                result.append(curr)
            else:
                curr = combine(prev, curr)
                result[-1] = curr
                
            if not noOverlap(curr, newInterval):
                result[-1] = combine(curr, newInterval)
                notAdded = False
            else:
                if (newInterval[0] < curr[0]) and notAdded:
                    result.insert(-1, newInterval)
                    notAdded = False

        if notAdded:
            result.append(newInterval)
            

        return result

def main() -> None:
    intervals: List[List[int]] = []
    newInterval: List[int] = [4,8]
    x = Solution().insert(intervals, newInterval)
    print(x)
    expected: List[List[int]] = [[4,8]]
    print (expected)

if __name__ == "__main__":
    main()
