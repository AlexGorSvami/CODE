class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        for a in sorted(asteroids):
            if mass < a: return False
            mass += a
        return True
