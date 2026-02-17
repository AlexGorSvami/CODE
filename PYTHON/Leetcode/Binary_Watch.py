def readBinaryWatch(turnedOn: int) -> list:
    answer = []
    for hour in range(12):
        for minute in range(60):
            if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                answer.append(f'{hour}:{minute:02d}')

    return answer 
