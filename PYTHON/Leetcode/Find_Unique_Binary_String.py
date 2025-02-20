def findDifferentBinaryString(nums: list) -> str:
    return ''.join(str(int(j[i]=='0')) for i, j in enumerate(nums))


print(findDifferentBinaryString(['01', '10']))
print(findDifferentBinaryString(['00', '01']))
print(findDifferentBinaryString(['111', '011', '001']))
