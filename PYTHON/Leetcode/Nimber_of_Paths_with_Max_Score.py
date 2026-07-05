from typing import List 
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        mod = 10**9 + 7 
        dp = [[[-1, 0] for _ in range(n + 1)] for _ in range(n + 1)]
        dp[n - 1][n - 1] = [0, 1]

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == 'X' or (r == n-1 and c == n-1):
                    continue 

                max_val = max(dp[r+1][c][0], dp[r][c+1][0], dp[r+1][c+1][0])
                if max_val != -1:
                    score = int(board[r][c]) if board[r][c] not in 'SE' else 0 
                    dp[r][c][0] = max_val + score 

                    for nr, nc in ((r + 1, c), (r, c + 1), (r + 1, c + 1)):
                        if dp[nr][nc][0] == max_val:
                            dp[r][c][1] = (dp[r][c][1] + dp[nr][nc][1]) % mod 

        return [dp[0][0][0] if dp[0][0][1] else 0, dp[0][0][1]]

