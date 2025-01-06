import re
def minion_game(word: str) -> None:
    """ Print the winner and the score"""
    player1 = player2 = 0
    length: int = len(word)
    for i, char in enumerate(word):
        points: int = length - i
        if char in ('A', 'E', 'I', 'O', 'U'):
            player1 += points
        else:
            player2 += points
    if player1 == player2:
        print('Draw')
    else: 
     print(*('Stuart', player2) if player2 > player1 else ('Kevin', player1))


def minion_game1(word: str) -> None:
    vowels = 'AEIOU'
    player1 = 0
    player2 = 0
    len_word = len(word)
    for i in range(len_word):
        if word[i] in vowels:
            player1 += len_word - i
        else:
            player2 += len_word - i
    if player1 > player2:
        print('Kevin', str(player1))
    elif player2 > player1:
        print('Stuart', str(player2))
    else:
        print('Draw')

def minion_game2(word:str) -> None:
    player1 = 0
    index = 0
    regex = '^[AEIOU]'
    len_word = len(word)
    for i in word:
        if bool(re.match(regex, i)):
            player1 = player1 + (len_word - index)
        index += 1
    player2 = (((len_word)*(len_word+1))/2) - player1
    if player1 > player2:
        print(f'Kevin',player1)
    elif player2 > player1:
        print('Stuart',int(player2))
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
    minion_game1(s)
    minion_game2(s)


