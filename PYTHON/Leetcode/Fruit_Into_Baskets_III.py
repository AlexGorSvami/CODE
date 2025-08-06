def numOfUnplacedFruits(fruits: list, baskets: list) -> int:
    from math import ceil, sqrt 
    busket_size = ceil(sqrt(len(fruits)))
    buskets = [[] for _ in range(busket_size)]
    for i, basket in enumerate(baskets):
        buskets[i // busket_size].append((basket, i))

    for busket in buskets:
        busket.sort()
        
    placed = 0 
    for fruit in fruits:
        for busket in buskets:
            if busket and busket[-1][0] >= fruit:
                chosen = min((i, basket) for basket, i in busket if basket >= fruit)
                busket.remove((chosen[1], chosen[0]))
                placed += 1 
                break 
    return len(fruits) - placed 

