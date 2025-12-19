class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # [10,2,-5]) == [10]
        i = 0
        j = 1
        result = []
        while j < len(asteroids):
            if j + 1 > len(asteroids):
                break
            elif asteroids[i] < 0:
                result.append(asteroids[i])
                i += 1
                j += 1
            elif asteroids[i] > 0 and asteroids[j] > 0:
                result.append(asteroids[i])
                i += 1
                j += 1
            elif asteroids[i] > 0 and asteroids[j] < 0:
                if asteroids[i] > abs(asteroids[j]):
                    result.append(asteroids[i])
                    i += 1
                    j += 1
                elif asteroids[i] < abs(asteroids[j]):
                    # result.append([asteroids[j]])
                    for n in range(len(result),-1,-1):
                        if result == []:
                            result.append(asteroids[j])
                        elif n < abs(asteroids[j]):
                            result.pop()
                        elif n > abs(asteroids[j]):
                            result.append(asteroids[j])
                            break
                    i += 2
                    j += 2
                else:
                    i += 2
                    j += 2
                
        return asteroids

r = Solution()
assert r.asteroidCollision([1,-2,-2,1]) == [-2,-2,1]  
assert r.asteroidCollision([8,-8]) == []
assert r.asteroidCollision([10,2,-5]) == [10]

print("Tests have passed.")  

# [-2,2,5,-11,5,6, -15]
# i = 0   
# while i < len(asteroids):
#             if i + 1 == len(asteroids):
#                 break
#             elif asteroids[i] < 0:
#                 i += 1
#             elif asteroids[i] > 0 and asteroids[i + 1] > 0:
#                 i += 1
#             elif asteroids[i] > 0 and asteroids[i + 1] < 0:
#                 if asteroids[i] > abs(asteroids[i + 1]):
#                     asteroids.pop(i + 1)
#                 elif asteroids[i] < abs(asteroids[i + 1]):
#                     asteroids.pop(i)
#                 else:
#                     asteroids.pop(i)
#                     asteroids.pop(i)
#                 i -= 1
#                 if i == -1:
#                     i = 0

#         return asteroids
