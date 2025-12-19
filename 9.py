class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()

        step = arr[1] - arr[0]

        for i in range(1,len(arr)-1):
            if step != arr[i+1] - arr[i]:
                return False

        return True
    
r = Solution()
assert r.canMakeArithmeticProgression([3,5,1]) == True
assert r.canMakeArithmeticProgression([1,2,4]) == False
assert r.canMakeArithmeticProgression([1,0]) == True

print("Tests have passed.")


        
