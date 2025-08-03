def maxTotalFruits(fruits: list, startPos: int, k: int) -> int:
    def step(fruits: list, startPos: int, left: int, right: int) -> int:
        return (min (
                    abs(startPos - fruits[right][0]),
                    abs(startPos - fruits[left][0]))
                    + fruits[right][0] - fruits[left][0])

    left, total, result = 0, 0, 0 

    for right in range(len(fruits)):
        total += fruits[right][1]

        while left <= right and step(fruits, startPos, left, right) > k:
            total -= fruits[left][1]
            left += 1 

        result = max(result, total)

    return result 
