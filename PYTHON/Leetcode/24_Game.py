def judgePoint24(self, cards: list) -> bool:
    if not cards: return False
    l = len(cards)
    if l == 1: return abs(cards[0] - 24) < 1e-6
    for i in range(l):
        for j in range(l):
            if i != j:
                nums = [cards[k] for k in range(l) if i != k and j != k]
                new_cards = [cards[i] - cards[j]]
                if i < j:
                    new_cards.extend([cards[i] + cards[j], cards[i] * cards[j]])
                if cards[j] != 0:
                    new_cards.append(cards[i] / float(cards[j]))
                for card in new_cards:
                    nums.append(card)
                    if self.judgePoint24(nums): return True
                    nums.pop()
    return False 
