def countLargestGroup(n: int) -> int:
    def get_num(n):
        result = 0
        while n != 0:
            result += n % 10
            n //= 10
        return result 
    
    array, m = [0] * 37, 0
    for i in range(1, n+1):
        curr = get_num(i)
        array[curr] += 1 
        if array[curr] > m:
            m = array[curr]
    count = 0 
    for i in range(37):
        if array[i] == m:
            count += 1 
    return count 

print(countLargestGroup(13))
print(countLargestGroup(2))
