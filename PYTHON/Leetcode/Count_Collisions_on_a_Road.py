def countCollisions(directions: str) -> int:
        if len(directions) == 0:
            return 0
        coll = 0
        direct  = directions[0]
        weight = 1
        i = 1
        while (i <len(directions)):
            if direct == "S":
                if directions[i] == "S":
                    weight = 1 
                elif directions[i] == "R":
                    direct = "R"
                    weight = 1 
                elif directions[i] == "L":
                    coll += 1
                    direct = "S"
            elif direct == "L":
                if directions[i] == "S":
                    direct = "S"
                    weight = 1
                elif directions[i] == "R":
                    direct = "R"
                    weight = 1
                elif directions[i] == "L":
                    weight = 1
            elif direct == "R":
                if directions[i] == "L":
                    coll += 2
                    # handle multiple cars going to right getting crashed with a car going left
                    while (weight > 1):
                        coll += 1
                        weight -= 1
                    direct = "S"
                elif directions[i] == "R":
                    weight += 1
                elif directions[i] == "S":
                    coll += 1
                    # handle multiple cars going to right getting crashed with a staying car
                    while (weight > 1):
                        coll += 1
                        weight -= 1
                    direct = "S"
            i += 1
        return coll
