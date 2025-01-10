class Solution:
    def eq(self, el1: List[int], el2: List[int]):
        equal = True
        for i in range(len(el1)):
            if (el1[i] != el2[i]):
                equal = False
        return equal
        
        
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        c = 0
        col = []
        ccol = []
        for i in range(n):
            for j in range(n):
                ccol.append(grid[j][i])
            col.append(ccol)
            ccol = []
            
        for i in range(n):
            for j in range(n):
                if self.eq(col[i], grid[j]):
                    c += 1
        return c
            