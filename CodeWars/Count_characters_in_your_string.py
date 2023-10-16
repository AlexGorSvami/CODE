from collections import Counter

def count(string):
    return Counter(string)

def count1(string):
  
    return {i: string.count(i) for i in string}
