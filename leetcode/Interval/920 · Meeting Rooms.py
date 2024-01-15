import copy
from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
       intervals.sort() 
       prev = intervals[0]
       for curr in intervals[1:]:
           if curr[0] < prev[1]:
               return False
            
       return True

def test(testCases):
    for testCase in testCases:
        ans = Solution().can_attend_meetings(testCase["input"])
        if ans != testCase["output"]:
            print(testCase["input"])
            print(f"exptected: {testCase['output']}")
            print(f"output: {ans}")
    
def main() -> None:
    testCases = []
    testCase = {}

    testCase["input"] = [(0,30),(5,10),(15,20)]
    testCase["output"] = False
    testCases.append(copy.copy(testCase))

    testCase["input"] = [(5,8),(9,15)]
    testCase["output"] = True
    testCases.append(copy.copy(testCase))

    
    test(testCases)

if __name__ == "__main__":
    main()