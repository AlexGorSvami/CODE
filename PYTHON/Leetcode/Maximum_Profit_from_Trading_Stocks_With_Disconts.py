def maxProfit(n: int, present: list, future: list, hierarchy: list, budget: int) -> int:
    g = [[] for _ in range(n)]
    for e in hierarchy:
        g[e[0]-1].append(e[1] - 1)

    def dfs(u: int):
        cost = present[u]
        d_cost = present[u] // 2 

        dp0 = [0] * (budget + 1)
        dp1 = [0] * (budget + 1)

        sub_profit0 = [0] * (budget + 1)
        sub_profit1 = [0] * (budget + 1)
        u_size = cost 

        for v in g[u]:
            child_dp0, child_dp1, v_size = dfs(v)
            u_size += v_size 
            for i in range(budget, -1, -1):
                for sub in range(min(v_size, i) + 1):
                    sub_profit0[i] = max(
                            sub_profit0[i],
                            sub_profit0[i - sub] + child_dp0[sub],
                            )
                    sub_profit1[i] = max(
                            sub_profit1[i],
                            sub_profit1[i - sub] + child_dp1[sub],
                            )

        for i in range(budget + 1):
            dp0[i] = sub_profit0[i]
            dp1[i] = sub_profit0[i]
            if i >= d_cost:
                dp1[i] = max(sub_profit0[i], sub_profit1[i - d_cost] + future[u] - d_cost)
            if i >= cost:
                dp0[i] = max(sub_profit0[i], sub_profit1[i - cost] + future[u] - cost)

        return dp0, dp1, u_size 
    
    return dfs(0)[0][budget] 

