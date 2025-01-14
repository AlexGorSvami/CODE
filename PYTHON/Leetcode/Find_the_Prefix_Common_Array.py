def findThePrefixCommonArray(A: list[int], B:list[int]) -> list[int]:
    set_A, set_B = set(), set()
    answer = []

    for i in range(len(A)):
        set_A.add(A[i])
        set_B.add(B[i])

        answer.append(len(set_A & set_B))

    return answer

print(findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))
print(findThePrefixCommonArray([2,3,1],[3,1,2]))
