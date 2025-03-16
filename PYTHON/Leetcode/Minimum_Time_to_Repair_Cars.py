def repairCars(ranks: list, cars: int) -> int:
    import math
    def is_repair_possible(min_time):
        car = 0
        for rank in ranks:
            car += int(math.sqrt(min_time/rank))
        return car >= cars 

    n = len(ranks)
    start, end = 1, 100*(10**6)**2
    while start < end:
        mid = start + (end - start) // 2 
        if is_repair_possible(mid):
            end = mid 
        else:
            start = mid + 1 
    return start 

print(repairCars([4,2,3,1], 10))
print(repairCars([5,1,8], 6))
