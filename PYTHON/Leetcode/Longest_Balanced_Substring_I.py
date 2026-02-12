def longestBalanced(s: str) -> int:
    n = len(s)
    answer = 0 

    for i in range(n):
        frequency = [0] * 26 

        for j in range(i, n):
            ind = ord(s[j]) - ord('a')
            frequency[ind] += 1 
            min_freq = float('inf')
            max_freq = 0 

            for k in frequency:
                if k > 0:
                    min_freq = min(min_freq, k)
                    max_freq = max(max_freq, k)

            if min_freq == max_freq:
                answer = max(answer, j - i + 1)

    return answer 
