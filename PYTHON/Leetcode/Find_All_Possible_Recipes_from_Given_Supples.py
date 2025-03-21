def findAllRecipes(recipes: list, ingredients: list, supplies: list) -> list:
    can_cook = {s: True for s in supplies}
    recepie_index = {r: i for i, r in enumerate(recipes)}

    def dfs(r):
        if r in can_cook:
            return can_cook[r]

        if r not in recepie_index:
            return False 
        can_cook[r] = False 

        for n in ingredients[recepie_index[r]]:
            if not dfs(n):
                return False 
        can_cook[r] = True 
        return can_cook 

    return [i for i in recipes if dfs(i)]

print(findAllRecipes(recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]))


