class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.group = defaultdict(list)
        self.max = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        f = self.count[val]
        if f > self.max:
            self.max = f
        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.max].pop()
        self.count[val] -= 1
        if not self.group[self.max]:
            self.max -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()