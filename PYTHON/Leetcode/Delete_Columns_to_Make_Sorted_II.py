def minDeletionSize(strs: list) -> int:
    ordered = [False] * (len(strs) - 1)
    result = 0 
    for i in range(len(strs[0])):
        col_ordered = [False] * (len(strs) - 1)
        has_conflict = False 
        for j in range(len(strs) - 1):
            if ordered[j]:
                continue 
            word1 = strs[j]
            word2 = strs[j + 1]
            if word1[i] < word2[i]:
                col_ordered[j] = True
            if word1[i] > word2[i]:
                has_conflict = True 
        if not has_conflict:
            for i in range(len(ordered)):
                ordered[i] = ordered[i] or col_ordered[i]
        else:
            result += 1 
    
    return result  
