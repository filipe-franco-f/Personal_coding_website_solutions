from array import *
from bisect import *
from collections import *
from typing import List

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for l in nums:
            l.sort()

        total = 0
        for i in range(len(nums[0])):
            rec = nums[0][-1]
            for j in range(len(nums)):
                rec = max(rec, nums[j].pop())
            total += rec
        return total
