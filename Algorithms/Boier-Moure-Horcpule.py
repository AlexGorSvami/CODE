# t = 'данные'
#
#  # Этап 1: формирование таблицы смещений
# S = set()
# M = len(t)
# d = {}
#
# for i in range(M-2, -1, -1):
#     if t[i] not in S:
#         d[t[i]] = M-i-1
#         S.add(t[i])
#
# if t[M-1] not in S:
#     d[t[M-1]] = M
#
# d['*'] = M
#
# print(d)
#
# # Этап 2: поиск образа в строке
#
# a = 'больште метеоданные'
# N = len(a)
#
# if N >= M:
#     i = M-1
#
#     while i < N:
#         k = 0
#         for j in range(M-1, -1, -1):
#             if a[i-k] != t[j]:
#                 if j == M-1:
#                     off = d[a[i]] if d.get(a[i], False) else d['*']
#                 else:
#                     off = d[t[j]]
#
#                 i += off
#                 break
#
#             k += 1
#
#         if j == 0:
#             print(f"образ найден по индексу {i-k+1}")
#             break
# else:
#     print('Образ  не найден')

def offse_table_generation(word: str) -> dict:
    uniq_symbols = set()
    len_symbols = len(word)
    offset_dict = {}

    for i in range(len_symbols-2, -1, -1): # итерация с последнего символа
        if word[i] not in uniq_symbols:
            offset_dict[word[i]] = len_symbols-i-1
            uniq_symbols.add(word[i])

    if word[len_symbols-1] not in uniq_symbols:
        offset_dict[word[len_symbols-1]] = len_symbols

    offset_dict['*'] = len_symbols

    return offset_dict

def find_image_in_text(word: str, text: str, offset_dict: dict) -> bool:
    len_text = len(text)
    len_word = len(word)

    if len_text >= len_word:
        count1 = len_word-1 # счетчик проверяемого символа в строке

        while count1 < len_text:
            count2 = 0
            for i in range(len_word-1, -1, -1):
                if text[count1-count2] != word[i]:
                    if i == len_word-1:
                        off = offset_dict[text[count1]] if offset_dict.get(text[count1], False) else offset_dict['*']
                    else:
                        off = offset_dict[word[i]]

                    count1 += off
                    break

                count2 += 1

            if i == 0:
                print(f"Образ найден по индексу {i-count2+1}")
                break

        else:
            print('Образ не найден')



find_image_in_text("данные", "большие методанные", offse_table_generation('данные'))







