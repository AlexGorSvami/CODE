def maxPower(stations: list, r: int, k: int) -> int:
        n = len(stations)

        diff = [0] * (n + 1)
        for i in range(n):
            left = max(0,  i - r)
            right = min(n, i + r + 1)
            diff[left] += stations[i]
            diff[right] -= stations[i]

        def can_archieve(min_power: int) -> bool:
            power_diff = diff.copy()
            cur_power = 0
            stations_left = k

            for c in range(n):
                cur_power += power_diff[c]

                if cur_power < min_power:
                    need = min_power - cur_power
                    if stations_left < need:
                        return False
                    
                    stations_left -= need

                    end = min(n, c + 2 * r + 1)
                    power_diff[end] -= need
                    cur_power += need
            return True
        
        left = min(stations)
        right = sum(stations) + k
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can_archieve(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
