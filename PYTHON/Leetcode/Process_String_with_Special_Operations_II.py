class Solution:
    def processStr(self, s: str, k: int) -> str:
        r = []
        for c in s:
            if c.isalpha(): r.append(c)
            elif c == '*' and r: r.pop()
            elif c == '#': r += r 
            elif c == '%': r.reverse()
        return r[k] if 0 <= k < len(r) else '.'
