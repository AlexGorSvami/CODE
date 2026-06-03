def min_finish_time(l_start, l_dur, w_start, w_dur):
    min_l_fin = min(s + d for s, d in zip(l_start, l_dur))
    min_w_fin = min(s + d for s, d in zip(w_start, w_dur))
    
    return min(
        min(max(min_l_fin, s) + d for s, d in zip(w_start, w_dur)),
        min(max(min_w_fin, s) + d for s, d in zip(l_start, l_dur))
    )
