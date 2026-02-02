def minimumCost(nums: list, k: int, dist: int) -> int:
        kk = k - 1
        sl = SortedList()
        win_sum = 0
        best = 1 << 63
        for i in range(1, len(nums)):
            n = nums[i]
            sl.add((n, i))

            idx = sl.index((n, i))
            if idx < kk:
                win_sum += n

                if len(sl) > kk:
                    win_sum -= sl[kk][0]
           if i - dist - 1 >= 1:
                j = i - dist - 1
                n = nums[j]
                if (n, j) in sl:
                    idx = sl.index((n, j))
                    sl.pop(idx)

                    if idx < kk:
                        win_sum -= n

                        if len(sl) >= kk:
                            win_sum += sl[kk - 1][0]

            if len(sl) >= kk:
                best = min(best, win_sum)

        return best + nums[0]
   
