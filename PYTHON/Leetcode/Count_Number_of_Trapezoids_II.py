def countTrapezoids(points: list) -> int:
        groups = defaultdict(list) 
        groups2 = defaultdict(list) 

        for i, (x, y) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y - y2
                dx = x - x2
                k = dy / dx if dx else math.inf
                b = (y * dx - x * dy) / dx if dx else x
                groups[k].append(b)
                groups2[(x + x2, y + y2)].append(k)

        ans = 0
        for g in groups.values():
            if len(g) == 1:
                continue
            s = 0
            for c in Counter(g).values():
                ans += s * c
                s += c

        for g in groups2.values():
            if len(g) == 1:
                continue
            s = 0
            for c in Counter(g).values():
                ans -= s * c 
                s += c

        return ans        
