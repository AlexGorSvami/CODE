class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        diff = abs((hour % 12) * 30 + minutes * 0.5 - minutes * 6)
        return min(diff, 360 - diff)
