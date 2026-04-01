def survivedRobotHealths(positions: list, healths: list, directions: str) -> list:
    robots = (sorted(zip(positions, healths, directions, range(len(positions)))))
    stack = []

    for pos, health, dir, ind in robots:
        if dir == 'R':
            stack.append((pos, health, dir, ind))
        else:
                while stack and stack[-1][-2] == 'R' and health > 0:
                r_pos, r_health, r_dir, r_ind = stack.pop()
                if r_health > health:
                    r_health -= 1 
                        stack.append((r_pos, r_health, r_dir, r_ind))
                    health = 0 
                elif r_health < health:
                    health -= 1 
                else:
                    health = 0 
            if health > 0:
                stack.append((pos, health, dir, ind))
    result = [0] * len(positions)
    for pos, health, dir, ind in stack:
        result[ind] = health 

    return [i for i in result if i > 0]
