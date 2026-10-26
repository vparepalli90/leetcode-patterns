"""
LC 1047 - Remove All Adjacent Duplicates in String (Easy)
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

Pattern: stack (cancel matching neighbors)
Idea:    Read from the input, write to a separate stack.
         If the new char equals stack[-1] (the most recent char still remaining), pop;
         otherwise push. Popping exposes older chars, so chain reactions happen
         automatically ("abba" -> "").
         Same template as LC 20 Valid Parentheses.
Time:    O(n)   Space: O(n)
"""


def remove_duplicates(s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)


if __name__ == "__main__":
    assert remove_duplicates("abbaca") == "ca"
    assert remove_duplicates("azxxzy") == "ay"
    assert remove_duplicates("aa") == ""
    assert remove_duplicates("abc") == "abc"
    assert remove_duplicates("abba") == ""
    assert remove_duplicates("") == ""
    print("lc1047 remove_duplicates: all tests passed")
