@cache
def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list:
    if firstPlayer + secondPlayer == n+1:
        return (1, 1)
    if firstPlayer > secondPlayer:
        return self.earliestAndLatest(n, secondPlayer, firstPlayer)
    if firstPlayer + secondPlayer > n + 1:
        return self.earliestAndLatest(n, n - secondPlayer+1, n - firstPlayer+1)

    min1 = float('inf')
    max1 = -float('inf')
    if secondPlayer > (n+1) // 2:
        second = n+1 - secondPlayer 
        x, y = firstPlayer-1, second - firstPlayer-1 
        z = (secondPlayer-1 - second+1) // 2 
        for i in range(x+1):
            for j in range(y+1):
                new = self.earliestAndLatest((n+1) // 2, i+1, i+1+j+z+1)
                min1 = min(min1, new[0]+1)
                max1 = max(max1, new[1] + 1)
    else:
        x, y = firstPlayer-1, secondPlayer - firstPlayer - 1 
        for i in range(x+1):
            for j in range(y+1):
                new = self.earliestAndLatest((n+1) // 2, i+1, i+1+j+1)
                min1 = min(min1, new[0] + 1)
                max1 = max(max1, new[1] + 1)
    return (min1, max1)
