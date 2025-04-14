def countGoodTriplets(arr: list, a: int, b: int, c: int) -> int:
    result = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) > a:
                continue 
            for k in range(j+1, len(arr)):
                if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    result += 1 
                    
    return result 



print(countGoodTriplets([3,0,1,1,9,7], 7, 2, 3))
print(countGoodTriplets([1,1,2,2,3], 0, 0, 1))
