from array import *
from bisect import *
from collections import *
from contextlib import closing
from typing import List

"()"
"(())" "()()"
"((()))" "(()())" "(())()" "()(())" "()()()"

class Solution:

    def append_new_parenthesis(self, s: str, new_level:dict):
        opening_turning_points = []
        closing_turning_points = []
        for p in range(len(s) - 1):
            if s[p] == "(" and s[p + 1] == ")":
                opening_turning_points.append(p)
                closing_turning_points.append(p + 1)
        #print(opening_turning_points)
        #print(closing_turning_points)
        for i in opening_turning_points:
            for b in closing_turning_points:
                if b >= i:
                    new_str = s[:i + 1] + "(" + s[i + 1:b + 1] + ")" + s[b + 1:]
                    # print(new_str)
                    if not new_str in new_level:
                        new_level[new_str] = 1
        new_level["()" + s] = 1


    def calculate_next(self, lis: dict):
        new_level = {}
        for s in lis[-1]:
            self.append_new_parenthesis(s, new_level)
        lis.append(new_level)

    def generateParenthesis(self, n: int) -> List[str]:
        lis = [{"()"}]
        for i in range(2, n + 1):
            self.calculate_next(lis)
            print(type(lis[-1]))
        return list(lis[-1].keys())

sol = Solution()
print(sol.generateParenthesis(5))
print(sol.generateParenthesis(4))
print(sol.generateParenthesis(2))
