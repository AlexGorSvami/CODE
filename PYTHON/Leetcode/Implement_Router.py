import unittest

from typing import *

from collections import defaultdict, deque
from bisect import bisect, bisect_left

class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.queue = deque()
        self.maps = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        k = [timestamp, source]
        i = bisect(self.maps[destination], k)
        if (1 <= i < len(self.maps[destination]) and self.maps[destination][i-1] == k 
            or (self.maps[destination] and self.maps[destination][-1] == k)):
            return False
        self.maps[destination].insert(i, k)

        self.queue.append((destination, k))
        if len(self.queue) > self.limit:
            destination, k = self.queue.popleft()
            i = bisect(self.maps[destination], k)
            self.maps[destination].pop(i-1)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        destination, k = self.queue.popleft()
        i = bisect(self.maps[destination], k)
        self.maps[destination].pop(i-1)
        return k[1], destination, k[0]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        l = self.maps[destination]
        left = bisect_left(l, [startTime, float('-inf')])
        right = bisect(l, [endTime, float('inf')])
        return right - left
