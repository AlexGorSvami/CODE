answer = {}
for i in range(int(input())):
    word = input()
    if word in answer:
        answer[word] += 1
    else:
        answer[word] = 1
print(len(answer))
print(' '.join([str(answer[word]) for word in answer]))
