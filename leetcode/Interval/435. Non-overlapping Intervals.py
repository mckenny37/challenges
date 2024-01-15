import copy
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort()
        prevInterval = intervals[0]

        for currInterval in intervals[1:]:
            def overlaps():
                #print(prevInterval + currInterval)
                return (currInterval[0] < prevInterval[1]) 

            if overlaps():
                result += 1
                prevInterval = currInterval if currInterval[1] < prevInterval[1] else prevInterval
            else:
                prevInterval = currInterval

        return result
    
def test(testCases) -> None:
    for testCase in testCases:
        ans = Solution().eraseOverlapIntervals(testCase["input"])
        if ans != testCase["expected"]:
            print(testCase["input"])
            print(ans)
            print(testCase["expected"])

def main() -> None:
    testCases = []
    testCase = {}

    testCase["input"] = [[-25322,-4602],[-35630,-28832],[-33802,29009],[13393,24550],[-10655,16361],[-2835,10053],[-2290,17156],[1236,14847],[-45022,-1296],[-34574,-1993],[-14129,15626],[3010,14502],[42403,45946],[-22117,13380],[7337,33635],[-38153,27794],[47640,49108],[40578,46264],[-38497,-13790],[-7530,4977],[-29009,43543],[-49069,32526],[21409,43622],[-28569,16493],[-28301,34058]]
    testCase["expected"] = 19
    testCases.append(copy.copy(testCase))
    test(testCases)

    testCase["input"] = [[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]]
    testCase["expected"] = 4
    testCases.append(copy.copy(testCase))

    testCase["input"] = [[1,100],[11,22],[1,11],[2,12]]
    testCase["expected"] = 2
    testCases.append(copy.copy(testCase))

    testCase["input"] = [[1,2],[2,3],[3,4],[1,3]]
    testCase["expected"] = 1
    testCases.append(copy.copy(testCase))
    
    testCase["input"] = [[1,2],[1,2],[1,2]]
    testCase["expected"] = 2
    testCases.append(copy.copy(testCase))

    testCase["input"] = [[1,2],[2,3]]
    testCase["expected"] = 0
    testCases.append(copy.copy(testCase))

if __name__ == "__main__":
    main()    
    