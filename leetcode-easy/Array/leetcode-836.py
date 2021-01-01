class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if any([
            rec1[0] == rec1[2],
            rec1[1] == rec1[3],
            rec2[0] == rec2[2],
            rec2[1] == rec2[3],
        ]): return False
        
        if any([
            rec1[0] >= rec2[2],
            rec1[1] >= rec2[3],
            rec2[0] >= rec1[2],
            rec2[1] >= rec1[3],
        ]
        ): return False
        return True
    #rec1 = [0,0,1,1], rec2 = [2,2,3,3]
        