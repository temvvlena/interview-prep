"""
https://leetcode.com/problems/count-collisions-on-a-road/
"""
class Solution:
    def countCollisions(self, directions: str) -> int:
        count = 0
        stack = []

        for char in directions:
			# if the stack is empty, and the direction is left, we just continue
            if not stack and char == 'L':
                continue
            # otherwise we add the direction in the stack ('S' or 'R') because they might lead to collisions
            elif not stack and char != 'L':
                stack.append(char)
			# stack is not empty
            else:
				# the top element in the stack
                cur = stack[-1]
				# cases that will not lead to collisions
                if char == cur or cur == 'S' and char == 'R' or cur == 'L' and char == 'S' or cur == 'L' and char == 'R':
                    stack.append(char)
				# collision happen but the top of the stack is already 'S' no need to append
                elif cur == 'S' and char == 'L':
                    count += 1
				# collision happen, append a 'S' at the top
                elif cur == 'R' and char == 'S':
                    count += 1
                    stack.pop()
                    stack.append('S')
				# collision happen, append a 'S' at the top
                elif cur == 'R' and char == 'L':
                    count += 2
                    stack.pop()
                    stack.append('S')
        # here, the stack only contains 'R' and 'S'
		# we only need to deal with the 'R' before 'S' case
        n = len(stack)
        i = 0
        while i < n:
            rs = 1
            if stack[i] == 'S':
                i += 1
            elif stack[i] == 'R':
                if i == n-1:
                    return count
                elif stack[i] != stack[i+1]:
                    count += 1
                    i += 1
                else:
                    while i < n-1 and stack[i] == 'R' and stack[i] == stack[i+1]:
                        rs += 1
                        i += 1
                    if i == n-1:
                        return count
                    else:
                        count += rs
                        i += 1
        return count