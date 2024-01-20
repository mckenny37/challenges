import copy
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
       start = sorted([i[0] for i in intervals])
       end = sorted([i[1] for i in intervals])
       count, res, s, e = 0,0,0,0
       while s < len(start):
         if start[s] < end[e]:
           count += 1
           s += 1
         else:
             count -= 1
             e += 1
         res = max(res, count)

       return res

def test(testCases):
    for testCase in testCases:
        ans = Solution().min_meeting_rooms(testCase["input"])
        if ans != testCase["output"]:
            print(testCase["input"])
            print(f"exptected: {testCase['output']}")
            print(f"output: {ans}")
    
def main() -> None:
    testCases = []
    testCase = {}

    testCase["input"] = [(0,30),(5,10),(15,20)]
    testCase["output"] = 2
    testCases.append(copy.copy(testCase))

    testCase["input"] = [(5,8),(9,15)]
    testCase["output"] = 1
    testCases.append(copy.copy(testCase))

    
    test(testCases)

if __name__ == "__main__":
    main()