class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def dfs(start):
           if start < 0 or start >= len(arr) or start in visited:
                return False 
           if arr[start] == 0:
                return True 
           visited.add(start)
           return dfs(start + arr[start]) or dfs(start-arr[start])
        
        return dfs(start)
