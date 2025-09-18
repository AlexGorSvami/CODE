from sortedcontainers import SortedList
class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.pool: list[tuple[int, int, int]] = SortedList()
        self.tasks: dict[int, tuple[int, int, int]] = dict()
        for task in tasks:
            user_id, task_id, priority = task
            self.pool.add((priority, task_id, user_id))
            self.tasks[task_id] = (priority, task_id, user_id)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.pool.add((priority, taskId, userId))
        self.tasks[taskId] = (priority, taskId, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        triplet: tuple[int, int, int] = self.tasks[taskId]
        self.pool.discard(triplet)
        self.pool.add((newPriority, triplet[1], triplet[2]))
        self.tasks[taskId] = (newPriority, triplet[1], triplet[2])

    def rmv(self, taskId: int) -> None:
        triplet: tuple[int, int, int] = self.tasks[taskId]
        del self.tasks[taskId]
        self.pool.discard(triplet)

    def execTop(self) -> int:
        if not self.pool:
            return -1
        triplet: tuple[int, int, int] = self.pool[-1]
        self.pool.discard(triplet)
        del self.tasks[triplet[1]]
        return triplet[-1]
