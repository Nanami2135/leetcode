class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = (0, 0)
        dir = (0, 1) # North

        # directions = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
        transitions = {
            (0, 1): [(-1, 0), (1, 0)],
            (0, -1): [(1, 0), (-1, 0)],
            (1, 0): [(0, 1), (0, -1)],
            (-1, 0): [(0, -1), (0, 1)]
        }
        
        for i in instructions:
            if i == "G":
                pos = (pos[0] + dir[0], pos[1] + dir[1])
            if i == "L":
                dir = transitions[dir][0]
            if i == "R":
                dir = transitions[dir][1]
            print(f'Instruction {i}: pos {pos} dir {dir}')
        
        # return (pos, dir)
    
        if pos == (0, 0):
            return True
        else:
            return dir != (0, 1)


s = Solution()
# iis = "GGLLGG"
# iis = "GLRLLGLL"
# iis = "GL"
iis = "GLGLGGLGL"
result = s.isRobotBounded(iis)
print(result)
