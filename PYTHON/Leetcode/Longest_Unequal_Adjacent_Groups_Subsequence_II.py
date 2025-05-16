def getWordsInLongestSubsequence(words: list, groups: list) -> list:
   n = len(words)
   dp = {} # word: (length, group, prev)
   last_word = ""
   max_len = 0
   for i in range(n):
       dp[words[i]] = (1, groups[i], "")
       for j in range(len(words[i])):
           for c in string.ascii_lowercase:
               prev = words[i][:j] + c + words[i][j+1:]
                   if prev in dp and dp[prev][0] >= dp[words[i]][0] and dp[prev][1] != groups[i]:
                       dp[words[i]] = (dp[prev][0]+1, groups[i], prev)
        if dp[words[i]][0] > max_len:
                max_len = dp[words[i]][0]
                last_word = words[i]
        
        max_seq = [''] * max_len
        word = last_word
        for i in range(max_len-1, -1, -1):
            max_seq[i] = word
            word = dp[word][2]
        return max_seq

