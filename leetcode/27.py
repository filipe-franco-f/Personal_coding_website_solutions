from array import *
from bisect import *
from collections import *
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        pos = 0
        while pos < len(nums):
            if nums[pos] == val:
                pos += 1
            nums[i] = nums[pos]
            i += 1
            pos += 1
        return nums

a = [2, 5, 2]
sol = Solution()
print(sol.removeElement(a, 2]))