def smallestNumber(pattern: str) -> str:
    from functools import reduce
    return ''.join(map(str, reduce(lambda x,y:x+[*range(y,len(x),-1)], (y for y,z in enumerate(pattern+'I',1) if z=='I'),[])))




print(smallestNumber('IIIDIDDD'))
print(smallestNumber('DDD'))
