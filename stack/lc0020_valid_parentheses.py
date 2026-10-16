"""
LC 20 - Valid Parentheses (Easy)
https://leetcode.com/problems/valid-parentheses/

Pattern: stack (last in, first out)
Idea:    Map each CLOSING bracket to its OPENING bracket.
         Closing: the top of the stack must be its opener -> pop; otherwise False.
         Opening: push.
         Valid only if every opener got closed -> stack is empty at the end.
Time:    O(n)   Space: O(n) (e.g. "((((((")
"""


def is_valid(s: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in pairs:
            if stack and stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return not stack


if __name__ == "__main__":
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("(())") is True
    assert is_valid("((") is False
    assert is_valid("([)]") is False
    print("lc0020 is_valid: all tests passed")
