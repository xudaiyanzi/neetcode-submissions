class StockSpanner:

    def __init__(self):
        stack = []
        self.record = []

    def next(self, price: int) -> int:
        self.record.append(price)
        n, count = len(self.record), 0

        for i in range(n - 1, -1, -1):
            if self.record[i] <= price:
                count += 1
            else:
                break
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)