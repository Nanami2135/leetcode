from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        firstInterval = intervals[0]

        result = []
        start = firstInterval[0]
        end = firstInterval[1]
        t = 1
        

        for n in intervals:
            if t != 0:
                if end < n[0]:
                    # result.append([start,end])
                    result.append([n[0],n[1]])
                    t -= 1
                
                elif end >= n[1]:
                    start = min(n[0], newInterval[0])
                    end = max(n[1], newInterval[1])
                else:
                    result.append([n[0],n[1]])
            else:
                result.append([n[0],n[1]])


        return result


        

r = Solution()
assert r.insert([[1,3],[6,9]],[2,5]) == [[1,5],[6,9]]
assert r.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]) == [[1,2],[3,10],[12,16]]
# assert r.searchInsert([1,3,5,6],7) == 4

print("Tests have passed.")