def maxCollectedFruits(fruits: list) -> int:
    n,g = len(fruits), cache(lambda i,j: 0 <= j < i < n and fruits[i][j] + max(g(i-1, j+1), g(i, j+1), g(i+1, j+1)) or 0)
    return sum(fruits[i][i] for i in range(n)) + g(n-1, 0) + (g.cache_clear(), fruits := [*zip(*fruits)], g(n-1, 0))[2]
