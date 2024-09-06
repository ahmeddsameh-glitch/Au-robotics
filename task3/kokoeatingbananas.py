from typing import List
from math import ceil
import ast


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += ceil(p / k)
            return hours <= h

        l = 1
        r = max(piles)
        while l <= r:
            middle = (l + r) // 2
            if k_works(middle):
                r = middle - 1
            else:
                l = middle + 1

        return l
