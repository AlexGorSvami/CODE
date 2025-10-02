def maxBottlesDrunk(numBottles: int, numExchange: int) -> int:
    answer, empty = 0, 0
    while numBottles > 0:
        answer += numBottles 
        empty += numBottles 
        numBottles = 0 
        while empty >= numExchange:
            empty -= numExchange 
            numBottles += 1 
            numExchange += 1 
    return answer 
