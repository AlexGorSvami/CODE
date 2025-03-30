def partitionLabels(s:str) -> list:
    letters = {}

    for i in range(len(s)):
        letters[s[i]] = i

    result = []
    start = 0
    end = letters[s[0]]

    for i in range(1, len(s)):
        if i > end:
            result.append(end - start + 1)
            start = i 
            
        end = max(end, letters[s[i]])

    result.append(end - start + 1)

    return result 


print(partitionLabels('ababcbcadefegdehijhklij'))
print(partitionLabels('eccbbbbdec'))
