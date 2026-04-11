def minimumDistance(nums: list) -> int:
    answer = float('inf')
    count = defaultdict(list)

    for index, num in enumerate(nums):
        count[num].append(index)
        if len(count[num]) >= 3:
            distance = (count[num][-1] - count[num][-3]) * 2 
            answer = min(answer, distance)

    if answer == float('inf'):
        return -1 
    return answer 
