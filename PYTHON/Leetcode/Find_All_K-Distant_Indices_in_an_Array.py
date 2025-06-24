def findDistantIndices(nums: list, key: int, k: int) -> list:
    key_indices = [i for i in range(len(nums)) if nums[i] == key]
    output_list = []

    for each in key_indices:
        lower_bound = max(0, each - k)
        upper_bound = min(len(nums)-1, each + k)

        for i in range(lower_bound, upper_bound+1):
            if abs(i - each) <= k:
                output_list.append(i)

    return sorted(set(output_list))
