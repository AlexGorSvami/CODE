class TrieNode:
    def __init__(self, length: int, idx: int):
        self.children = {}
        self.best_len = length
        self.best_idx = idx

class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        # Находим минимальную длину и индекс для корня (соответствует пустому суффиксу)
        min_len = float('inf')
        min_idx = -1
        for i, w in enumerate(wordsContainer):
            if len(w) < min_len:
                min_len = len(w)
                min_idx = i
                
        root = TrieNode(min_len, min_idx)
        
        # Строим Trie по перевернутым строкам
        for i, w in enumerate(wordsContainer):
            curr = root
            for char in reversed(w):
                if char not in curr.children:
                    curr.children[char] = TrieNode(len(w), i)
                curr = curr.children[char]
                
                # Обновляем лучшие показатели узла
                if len(w) < curr.best_len:
                    curr.best_len = len(w)
                    curr.best_idx = i
                    
        # Ищем ответы для запросов
        ans = []
        for q in wordsQuery:
            curr = root
            for char in reversed(q):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break
            ans.append(curr.best_idx)
            
        return ans
