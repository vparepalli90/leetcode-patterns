"""
LC 155 - Min Stack (Medium)
https://leetcode.com/problems/min-stack/

Pattern: stack (design problem)
Idea:    Each entry stores (val, running_min), like a running-MIN column in SQL:
           MIN(val) OVER (ORDER BY row ROWS UNBOUNDED PRECEDING)
         getMin reads the last row. Popping never needs a recalculation, because
         the row underneath already knows the minimum at that point.
Time:    O(1) for every operation   Space: O(n) (space traded for time)
"""


class MinStack:
    def __init__(self):
        self.stack = []  # list of (val, running_min) pairs

    def push(self, val: int) -> None:
        if not self.stack:
            running_min = val
        else:
            running_min = min(val, self.stack[-1][1])
        self.stack.append((val, running_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    s = MinStack()
    s.push(5); s.push(3); s.push(7); s.push(2)
    assert s.getMin() == 2 and s.top() == 2
    s.pop(); assert s.getMin() == 3 and s.top() == 7
    s.pop(); assert s.getMin() == 3
    s.pop(); assert s.getMin() == 5

    s = MinStack()  # duplicates
    s.push(2); s.push(2); s.pop()
    assert s.getMin() == 2

    s = MinStack()  # LeetCode example
    s.push(-2); s.push(0); s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0 and s.getMin() == -2
    print("lc0155 MinStack: all tests passed")
