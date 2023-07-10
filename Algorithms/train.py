# t = 'лилила'
#
# p = [0] * len(t)
# j = 0
# i = 1
#
# while i < len(t):
#     if t[j] == t[i]:
#         p[i] = j + 1
#         i += 1
#         j += 1
#     else:
#         if j == 0:
#             p[i] = 0
#             i += 1
#         else:
#             j = p[j-1]
#
# print(p)
#
# a = 'лилилось лилилась'
# m = len(t)
# n = len(a)
#
# i = 0
# j = 0
#
# while i < n:
#     if a[i] == t[j]:
#         i += 1
#         j += 1
#         if j == m:
#             print('образ найден')
#             break
#     else:
#         if j > 0:
#             j = p[j - 1]
#         else:
#              i += 1
#
# if i == n:
#     print('образ найден')

# word = 'лилила'
#
# def array_of_matching_characters1(word: str):
#     array = [0] * len(word)
#     count1 = 0
#     count2 = 1
#
#     while count2 < len(word):
#         if word[count1] == word[count2]:
#             array[count2] = count1 + 1
#             count2 += 1
#             count1 += 1
#
#         else:
#             if count1 == 0:
#                 array[count2] = 0
#                 count2 += 1
#             else:
#                 count1 = array[count1-1]
#
#     return array
#     
#
# def find_image_in_str(word:str, text:str, array:list):
#     len_word = len(word)
#     len_text = len(text)
#
#     count1 = 0
#     count2 = 0
#
#     while count1 < len_text:
#         if text[count1] == word[count2]:
#             count1 += 1
#             count2 += 1
#             if count2 == len_word:
#                 return True
#         else:
#             if count2 > 0:
#                 count2 = array[count2-1]
#             else:
#                 count1 += 1
#
#     if count1 == len_text:
#         return False
#
#
# print(find_image_in_str(word, 'лилила лилилась', array_of_matching_characters1(word)))
#
#
# Алгоритм  KMP
# Этап 1. Формируем массив для сдвига по префиксам:
# def array_of_matching_characters(word):
#     array = [0] * len(word)
#     cnt1 = 0
#     cnt2 = 1
#
#     while cnt2 < len(word):
#         if word[cnt1] == word[cnt2]:
#             array[cnt2] = cnt1 + 1
#             cnt2 += 1
#             cnt1 += 1
#         else:
#             if cnt1 == 0:
#                 array[cnt2] = 0
#                 cnt2 += 1
#             else:
#                 cnt1 = array[cnt1 -1]
#
#     return array # сложность O(m)
#
# # Этап 2. Поиск образа в строке
#
# def find_image_in_text(word: str, text:str, array:list):
#     len_word = len(word)
#     len_text = len(text)
#
#     count1 = 0
#     count2 = 0
#     while count1 < len_text:
#         if text[count1] == word[count2]:
#             count1 += 1
#             count2 += 1
#             if count2 == len_word:
#                 return 'Image is found!' 
#         else:
#             if count2 > 0:
#                 count2 = array[count2 - 1]
#             else:
#                 count1 += 1
#     if count1 == len_text:
#         return 'Image is not found!'
#
# print(array_of_matching_characters('лилила'))        
# print(find_image_in_text('лилила', 'лиллилось лилилась', array_of_matching_characters('лилила')))


def array_of_matching_characters(word: str) -> list:
    array = [0] * len(word)
    cnt1 = 0
    cnt2 = 1

    while cnt2 < len(word):
        if word[cnt1] == word[cnt2]:
            array[cnt2] = cnt1 + 1
            cnt1 += 1
            cnt2 += 2
        else:
            if cnt1 == 0:
                array[cnt2] = 0
                cnt2 += 1
            else:
                cnt1 = array[cnt1-1]

    return array


def find_image_in_text(word: str, text: str, array: list) -> str:
    len_word = len(word)
    len_text = len(text)
    count1 = 0
    count2 = 0

    while count1 < len_text:
        if text[count1] == word[count2]:
            count1 += 1
            count2 += 1
            if count2 == len_word:
                return 'Image is found'
        else:
            if count2 > 0:
                count2 = array[count2 - 1]
            else:
                count1 += 1
    if count1 == len_text:
        return 'Image is not found'


print(find_image_in_text('лилила', 'лилилось лилилась', array_of_matching_characters('лилила')))





