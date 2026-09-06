class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1

        while self.stack:
            val, val_count = self.stack[-1]
            if val <= price:
                self.stack.pop()
                count += val_count
            else: 
                break
        self.stack.append((price, count))
    
        return count


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)