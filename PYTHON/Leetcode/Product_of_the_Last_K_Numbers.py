class ProductOfNumbers:

    def __init__(self):
        self.prefix_sum: List[int] = []

    def add(self, num: int) -> None:
        if not num:
            self.prefix_sum.clear()
            return
        self.prefix_sum.append(num * (self.prefix_sum[-1] if self.prefix_sum else 1))

    def getProduct(self, k: int) -> int:
        n: int = len(self.prefix_sum)
        if n < k: return 0
        elif n == k: return self.prefix_sum[-1]
        return self.prefix_sum[n - 1] // self.prefix_sum[n - k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(num)
param_2 = obj.getProduct(k)
