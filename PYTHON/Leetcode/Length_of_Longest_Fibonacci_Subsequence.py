def lenLongestFibSubseq(arr: list) -> int:
    longest = 0
    numbers = set(arr)

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            last, aim = arr[j], arr[i] + arr[j]
            count = 2

            while aim in numbers:
                count += 1
                last, aim = aim, last + aim 

            if count >= 3:
                longest = max(longest, count)

    return longest 



print(lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print(lenLongestFibSubseq([1,3,7,11,12,14,18]))

