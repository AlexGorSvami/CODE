def beeramid(bonus, price):
    beers = bonus / price
    level = 0

    while (level + 1)**2 <= beers:
        level += 1
        beers -= level**2

    return level
