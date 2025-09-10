def minimuteachings(n: int, languages: list, friendships: list) -> int:
    know = [set(i) for i in languages]
    need = set()
    for i, j in friendships:
        if know[i-1] & know[j-1]:
            continue 
        need.add(i-1)
        need.add(j-1)
    count = [0] * (n+1)
    for i in need:
        for j in languages[i]:
            count[j] += 1 
    return len(need) - max(count)
