def numSubmat(mat: list) -> int:
    if not mat:
        return 0
    m, n = len(mat), len(mat[0])
    h = [[0]*n for _ in range(m)]
    result = 0

    for i in range(m):
        st = []
        count = [0] * n 
        index = [-1] * n 
        for j in range(n-1, -1, -1):
            if i == 0:
                h[i][j] = mat[i][j]
            else:
                h[i][j] = 1 + h[i-1][j] if mat[i][j] == 1 else 0 
            while st and h[i][st[-1]] > h[i][j]:
                index[st.pop()] = j 
            st.append(j)
        
        for k in range(n):
            p = index[k]
            count[k] = h[i][k]*(k - p)
            if p != -1:
                count[k] += count[p]
            result += count[k]
    
    return result 
