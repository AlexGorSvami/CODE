class Fancy:

    def __init__(self):
        self.val = []
        self.mul = [1]
        self.add = [0]

    def append(self, val: int) -> None:
        self.val.append(val)
        self.add.append(self.add[-1])
        self.mul.append(self.mul[-1])


    def addAll(self, inc: int) -> None:
        self.add[-1] += inc 

    def multAll(self, m: int) -> None:
        self.mul[-1] *= m 
        self.add[-1] *= m 

    def getIndex(self, idx: int) -> int:
        MOD = 10 ** 9 + 7
        if 0 <= idx < len(self.val):
            mul = self.mul[-1] // self.mul[idx]
            add = self.add[-1] - self.add[idx] * mul 
            return (self.val[idx] * mul + add) % MOD 
        return -1

