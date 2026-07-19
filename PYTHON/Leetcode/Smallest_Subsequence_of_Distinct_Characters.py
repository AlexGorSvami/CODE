class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_oc = {c: i for i, c in enumerate(s)}
        stack, visited = [], set()

        for i, c in enumerate(s):
            if c in visited:
                continue 
            while stack and c < stack[-1] and i < last_oc[stack[-1]]:
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)

        return ''.join(stack)
