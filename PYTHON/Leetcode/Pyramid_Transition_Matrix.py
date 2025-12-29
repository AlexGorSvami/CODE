def pyramidTransition(bottom: str, allowed: list) -> bool:
    dic = defaultdict(lambda: defaultdict(list))
    for a, b, c in allowed:
        dic[a][b].append(c)

    def helper(bottom):
        return len(bottom) == 1 or any(
                helper(i)
                for i in product(*(dic[a][b] for a, b in zip(bottom, bottom[1:])))
                )

    return helper(bottom)


