def minDeletionSize(strs: list) -> int:
    return len([i for i in zip(*strs) if list(i) != sorted(i)])
