def numRabiits(answers: list) -> int:
    import collections 

    count = collections.Counter(answers)
    return sum((((i+1)+j-1)//(i+1))*(i+1) for i, j in count.items())


print(numRabiits([1,1,2]))
print(numRabiits([10,10,10]))
