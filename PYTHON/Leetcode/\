def matchPlayersAndTrainers(players: list, trainers: list) -> int:
    players.sort()
    trainers.sort()
    left = 0
    right = 0
    while left < len(players) and right < len(trainers):
        if players[left] <= trainers[right]:
            left += 1 
        right += 1 
    return left 
