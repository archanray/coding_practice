class MinStack:
    """
    Time complexity is O(1)
    Space complexity is O(n)
    """
    def __init__(self):
        self.s = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.s.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self) -> None:
        if not self.s:
            return
        self.s.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

class MinStack:
    """
    Time complexity is O(1)
    Space complexity is O(1)
    """
    def __init__(self):
        self.s = []
        self.minval = float("inf")

    def push(self, val: int) -> None:
        if not self.s:
            self.s.append(0)
            self.minval = val
        else:
            self.s.append(val - self.minval)
            if val < self.minval:
                self.minval = val

    def pop(self):
        if not self.s:
            return
        popval = self.s.pop()
        if popval < 0:
            self.minval = self.minval - popval

    def top(self) -> int:
        top = self.s[-1]
        if top > 0:
            return top + self.minval
        else:
            return self.minval

    def getMin(self) -> int:
        return self.minval