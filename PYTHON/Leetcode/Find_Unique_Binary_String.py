def findDifferentBinaryString(nums: list) -> str:
    return ''.join(str(int(j[i]=='0')) for i, j in enumerate(nums))

def findDifferentBinaryString1(nums: list) -> str:
    n = len(nums[0])
    for i in range(2**n):
        i = format(i, '0' + str(n) + 'b')
        if i not in nums:
            return i
print(findDifferentBinaryString(['01', '10']))
print(findDifferentBinaryString(['00', '01']))
print(findDifferentBinaryString(['111', '011', '001']))
