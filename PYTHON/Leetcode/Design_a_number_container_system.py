from collections import defaultdict
import heapq

class NumberContainers:

    def __init__(self):
        self.map = {}
        self.reverse_map = defaultdict(set)
        self.reverse_heap = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if index in self.map:
            pre = self.map[index]
            self.reverse_map[pre].remove(index)

        self.map[index] = number
        self.reverse_map[number].add(index)
        heapq.heappush(self.reverse_heap[number], index)

    def find(self, number: int) -> int:
        while len(self.reverse_heap[number]) > 0 and self.reverse_heap[number][0] not in self.reverse_map[number]:
            heapq.heappop(self.reverse_heap[number])

        return self.reverse_heap[number][0] if len(self.reverse_heap[number]) > 0 else -1
