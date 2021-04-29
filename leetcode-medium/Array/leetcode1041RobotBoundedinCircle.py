"""
Robot Bounded In Circle
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:
"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.
Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        pseudocode
        [north, right, down, left]
           ^                  
        north -> 0, 1
        right --> 1, 0
        down --> 0, -1
        left --> -1, 0
        direction --> down
        position --> {0, 0}
        buh string eeree loop hiigeed:
            hervee go baival:
                position += myList[direction] 
            hervee L baival:
                direction -= 1
                hervee direction ni 0 oos baga baival:
                    direction = len(mylist) - 1
            hervee R baival:
                direction += 1
                hervee direction ni len(myList) oos baga baival:
                    direction = 0
        hervee anhni position ni {0, 0} baival True
        hervee north oos oor chiglel baival True
        return False
        """
        
        myList = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction = 0
        position = [0, 0]
        for i in range(len(instructions)):
            
            if instructions[i] == "G":
                position[0] += myList[direction][0]
                position[1] += myList[direction][1]
            if instructions[i] == "L": direction -= 1
            if instructions[i] == "R": direction += 1
            direction = (direction + 4) % 4
        if position == [0,0]: return True
        if direction != 0: return True
        return False
        """
        myList = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction = 0
        position = [0, 0]
        for i in range(len(instructions)):
            if instructions[i] == "G":
                position[0] += myList[direction][0]
                position[1] += myList[direction][1]
            if instructions[i] == "L":
                if direction == 0:
                    direction = 3
                else: 
                    direction -= 1
            if instructions[i] == "R":
                if direction == 3:
                    direction = 0 
                else: 
                    direction += 1
        if position == [0,0]: return True
        if direction != 0: return True
        return False 
        """