def bestClosingTime(customers:str) -> int:
    answer, profit, max_profit = 0, 0, 0 

    for i, customer in enumearte(customers):
        profit += 1 if customer == 'Y' else -1 
        if profit > max_profit:
            max_profit = profit 
            answer = i + 1 

    return answer 
